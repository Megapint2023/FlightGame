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

        let weatherText = "- sää ei saatavilla...";

        if (data.weather && data.weather.temp !== undefined) {
            const w = data.weather;
            const windText = (w.wind !== undefined) ? `, wind ${w.wind} m/s` : "";
            weatherText = `- ${w.temp.toFixed(1)}°C, ${w.description}${windText}`;
        }

        document.getElementById("weather").innerText = weatherText;
        update_stats(data);
        if (data.found === true) {
          const gain = document.getElementById("point_gain");
          gain.classList.add("show");
          setTimeout(() => gain.classList.remove("show"), 900);
}
        await updateHiddenLocation();
        updateNavigator(airport.lat, airport.lon);
    })
    .catch(error => {
        console.error("Move failed:", error);
        document.getElementById("weather").innerText = "- sää ei saatavilla...";
    });
}