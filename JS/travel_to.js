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
        // SÄÄN PÄIVITTÄMINEN
        let weatherText = "- sää ei saatavilla...";
        if (data.weather && data.weather.temp !== undefined) {
            const w = data.weather;
            const windText = (w.wind !== undefined) ? `, wind ${w.wind} m/s` : "";
            weatherText = `- ${w.temp.toFixed(1)}°C, ${w.description}${windText}`;
        }
        document.getElementById("weather").innerText = weatherText;
        update_stats(data); // PÄIVITTYY STATUS PANEELIN JA SIJINTI ELEMNTIN

        // VÄLÄHDYS KYSEISEN SIIRRON ELI LENNON HINTA
        const lennonhinta = document.getElementById("lennonhinta");
        lennonhinta.textContent = `-${data.ticket_cost} €`;
        lennonhinta.classList.add("show");
        setTimeout(() => lennonhinta.classList.remove("show"), 900);

        // VÄLÄHDYS AINA KUN SAA PISTEEN
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