'use strict';

const options = { enableHighAccuracy: true, timeout: 5000, maximumAge: 0 };
let map, marker;

// NOUTAA LENTOKENTTÄ PISTEET NÄKYVIIN
let airports = [];

async function loadAirports() {
    const res = await fetch("http://127.0.0.1:5000/airports");
    airports = await res.json();

    airports.forEach(ap => {
        L.circleMarker([ap.lat, ap.lon], {
            radius: 6,
            color: '#000',
            fillColor: '#0f0',
            fillOpacity: 0.8
        }).addTo(map)
          .bindPopup(`${ap.name} (${ap.icao})`);
    });
}

// KARTTA - ASETTAA EUROOPALLE NS. RAJAUKSEN
const europeBounds = [[25, -25], [72, 45]];

// KARTTA "OSIO
function success(pos) {
    const crd = pos.coords;
    map = L.map('map', { maxBounds: europeBounds }).setView([crd.latitude, crd.longitude], 5);

    // HIENOMPI KARTTA (google earth)
    L.tileLayer(
      'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
      { attribution: 'Tiles &copy; Esri' }
    ).addTo(map);

    // FUNKTIO KUTSU -> QUERYN PALAUTETUT LENTOKENTÄT NÄKYVIIN
    loadAirports();

    // PELAAJA PINNI
    marker = L.marker([crd.latitude, crd.longitude])
        .addTo(map)
        .bindPopup("Pelaaja")
        .openPopup();

    updateNavigator(crd.latitude, crd.longitude);
    map.on('click', handleMapClick);
}

function error(err) {
  console.warn(err);
}

// KARTTA KLIKKAAMALLA LIIKKUMINEN
async function handleMapClick(e) {
    const { lat, lng } = e.latlng;

    let nearest = airports[0];
    let minDist = distance(lat, lng, nearest.lat, nearest.lon);

    airports.forEach(ap => {
        const d = distance(lat, lng, ap.lat, ap.lon);
        if (d < minDist) {
            nearest = ap;
            minDist = d;
        }
    });
    travel_to(nearest);

    // NÄYTTÄÄ PISTEINÄ SIJAINNIT KARTALLA (vihreät pisteet)
    const url = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${nearest.lat}&lon=${nearest.lon}`;
    const response = await fetch(url);
    const result = await response.json();
    const locationName =
        result.address?.city ||
        result.address?.town ||
        result.address?.village ||
        result.address?.country ||
        nearest.name;

    // PÄIVITTÄÄ PINNIN JA KESKITTÄÄ KARTAN
    marker.setLatLng([nearest.lat, nearest.lon]);
    map.setView([nearest.lat, nearest.lon], 5);
    marker.bindPopup(nearest.name).openPopup();
    updateNavigator(nearest.lat, nearest.lon);

}
// KARTALLA LIIKKUMINEN
function distance(lat1, lon1, lat2, lon2) {
  return Math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2);
}

navigator.geolocation.getCurrentPosition(success, error, options);