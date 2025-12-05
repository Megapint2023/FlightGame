'use strict';

function travel_to(airport) {
    fetch('http://127.0.0.1:5000/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            icao: airport.icao,
            distance: 1000,
            municipality: airport.name
        })
    })
    .then(response => response.json())
    .then(data => {
        update_stats(data);
        document.getElementById("weather").textContent = `Weather: ${data.weather}`;
    })
    .catch(err => console.error("Move failed:", err));
}