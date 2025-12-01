'use strict';


const options = { enableHighAccuracy: true, timeout: 5000, maximumAge: 0 };

let map, marker;


function success(pos) {
  const crd = pos.coords;
  map = L.map('map').setView([crd.latitude, crd.longitude], 5);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  marker = L.marker([crd.latitude, crd.longitude])
            .addTo(map)
            .bindPopup("I am here.")
            .openPopup();
}

function error(err) {
  console.warn(err);
}

navigator.geolocation.getCurrentPosition(success, error, options);


document.getElementById('input_button')
  .addEventListener('click', async () => {

    const query = document.getElementById('input_field').value;
    if (!query) return;

    const url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query)}`;
    const response = await fetch(url);
    const results = await response.json();

    if (results.length === 0) {
      alert("Location not found!");
      return;
    }

    const { lat, lon } = results[0];
    const newLatLng = [parseFloat(lat), parseFloat(lon)];

    marker.setLatLng(newLatLng);
    map.setView(newLatLng, 5);
    marker.bindPopup(query).openPopup();
});