'use strict';

// const hiddenLocation = { lat: 41.9028, lon: 12.4964 };

const hiddenLocation = null;

function updateNavigator(playerLat, playerLon) {
    const dy = hiddenLocation.lat - playerLat;
    const dx = hiddenLocation.lon - playerLon;

    const angle = Math.atan2(dx, dy) * (180 / Math.PI);

    document.getElementById("nav_arrow").style.transform = `rotate(${angle}deg)`;
    document.getElementById("nav_text").textContent = "Vihje: laukun signaalin suunta!";
}