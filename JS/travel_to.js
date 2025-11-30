let map, marker;

// Initialize map (same as before)
navigator.geolocation.getCurrentPosition(pos => {
  const crd = pos.coords;
  map = L.map('map').setView([crd.latitude, crd.longitude], 5);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

  marker = L.marker([crd.latitude, crd.longitude]).addTo(map)
           .bindPopup("I am here.")
           .openPopup();
}, err => console.warn(err));

// Handle MOVE button
document.getElementById('input_button').addEventListener('click', async () => {
  const query = document.getElementById('input_field').value;
  if (!query) return;

  // Use Nominatim to get coordinates from name
  const url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query)}`;
  const response = await fetch(url);
  const results = await response.json();
  if (results.length === 0) {
    alert("Location not found!");
    return;
  }

  const { lat, lon } = results[0];
  const newLatLng = [parseFloat(lat), parseFloat(lon)];

  // Move the marker
  marker.setLatLng(newLatLng);
  map.setView(newLatLng, 5); // zoom to new location
  marker.bindPopup(query).openPopup();
});