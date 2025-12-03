'use strict';

const options = { enableHighAccuracy: true, timeout: 5000, maximumAge: 0 };
let map, marker;

// NOUTAA LENTOKENTTÄ PISTEET KARTALLE
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
// EUROOPAN RAJAUS (testissä)
const europeBounds = [[34, -25], [72, 45]];

// KARTAN OMINAISUUDET
function success(pos) {
    const crd = pos.coords;
    map = L.map('map', { maxBounds: europeBounds }).setView([crd.latitude, crd.longitude], 5);

    // HIENOMPI KARTTA (kuin google earth)
    L.tileLayer(
      'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
      { attribution: 'Tiles &copy; Esri' }
    ).addTo(map);

    // Funktiokutsu querylle -> lataa lentokentät
    loadAirports();

    // Pelaajan markkeri
    marker = L.marker([crd.latitude, crd.longitude])
        .addTo(map)
        .bindPopup("I am here.")
        .openPopup();

    // Klikkaus kartalla
    map.on('click', handleMapClick);
}

function error(err) {
  console.warn(err);
}

// OSA 2 KARTALLA KLIKKAAMINEN
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

    // Noutaa sijainnin (TYÖN ALLA)
    const url = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${nearest.lat}&lon=${nearest.lon}`;
    const response = await fetch(url);
    const result = await response.json();
    const locationName =
        result.address?.city ||
        result.address?.town ||
        result.address?.village ||
        result.address?.country ||
        nearest.name;

    // PÄIVITTÄÄ pinnin JA KESKITTÄÄ KARTAN
    marker.setLatLng([nearest.lat, nearest.lon]);
    map.setView([nearest.lat, nearest.lon], 5);
    marker.bindPopup(locationName).openPopup();

    // PÄIVITTÄÄ PELIN STATUKSEN (panel_1)
    const travelCost = Math.floor(Math.random() * (275 - 93 + 1)) + 93;
    gameState.cash -= travelCost;
    gameState.points += 1;
    gameState.totalDistance += Math.floor(Math.random() * 1000);
    gameState.totalCO2 += Math.floor(Math.random() * 100);
    gameState.currentLocation = locationName;

    await fetchWeather(locationName);
    updateStatusPanel();
}

// FUNKTIO ETÄISYYDEN LASKEMISEEN
function distance(lat1, lon1, lat2, lon2) {
  return Math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2);
}

navigator.geolocation.getCurrentPosition(success, error, options);