'use strict';

function travel_to(airport) {
    fetch('/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            icao: airport.icao || airport.name,
            distance: distance(playerLat, playerLon, airport.lat, airport.lon)
        })
    })
    .then(response => response.json())
    .then(data => {
        update_stats(data);
    })
    .catch(err => console.error("Move failed:", err));
}