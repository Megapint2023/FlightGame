'use strict';

async function travel_to(airport) {
    fetch('http://127.0.0.1:5000/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            icao: airport.icao,
        })
    })
    .then(response => response.json())
    .then(async data => {
        const weather = data.weather;
        const teksti = weather.wind ? `, wind ${weather.wind} m/s` : "";

        document.getElementById("weather").innerText =
            `- ${weather.temp.toFixed(1)}°C, ${weather.description}${teksti}`;

        update_stats(data);
        await updateHiddenLocation();
        updateNavigator(airport.lat, airport.lon);
    })
    .catch(error => {
        console.error("Move failed:", error);
        document.getElementById("weather").innerText = "- sää ei saatavilla...";
    });
}