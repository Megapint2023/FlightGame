// INPUT NAPPI (jos haluaa syöttää matkakohteen)
document.getElementById('input_button').addEventListener('click', async () => {
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
    marker.setLatLng([lat, lon]);
    map.setView([lat, lon], 5);
    marker.bindPopup(query).openPopup();

    const travelCost = Math.floor(Math.random() * (275 - 93 + 1)) + 93;
    gameState.cash -= travelCost;
    gameState.points += 1;
    gameState.totalDistance += Math.floor(Math.random() * 1000);
    gameState.totalCO2 += Math.floor(Math.random() * 100);
    gameState.currentLocation = query;

    await fetchWeather(query);
    updateStatusPanel();
});
navigator.geolocation.getCurrentPosition(success, error, options);