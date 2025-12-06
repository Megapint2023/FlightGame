'use strict';

function travel_to(airport) {
    fetch('http://127.0.0.1:5000/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            icao: airport.icao,
            distance: 1000,

        })
    })
    .then(response => response.json())
    .then(data => {
            const weather = data.weather;
            const teksti = weather.wind ? `, wind ${weather.wind} m/s` : "";
            document.getElementById("weather").innerText =
                `WEATHER: ${weather.temp.toFixed(1)}°C, ${weather.description}${teksti}`;
        update_stats(data);
    })
    .catch(error => {
        console.error("Move failed:", error);
        document.getElementById("weather").innerText = "Ei saatavilla...";
    });
}