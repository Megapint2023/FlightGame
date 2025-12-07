'use strict';

let hiddenLocation = { lat: 0, lon: 0 };

function updateHiddenLocation() {
    return fetch('http://127.0.0.1:5000/current_suitcase')
        .then(response => response.json())
        .then(data => {
            hiddenLocation.lat = data.lat;
            hiddenLocation.lon = data.lon;
        })
        .catch(error => {
            console.error("Failed to fetch suitcase location:", error);
        });
}

function updateNavigator(playerLat, playerLon) {
    const dy = hiddenLocation.lat - playerLat;
    const dx = hiddenLocation.lon - playerLon;

    const angle = Math.atan2(dx, dy) * (180 / Math.PI);

    document.getElementById("nav_arrow").style.transform = `rotate(${angle}deg)`;
    document.getElementById("nav_text").textContent = "Vihje: laukun signaalin suunta!";
}
