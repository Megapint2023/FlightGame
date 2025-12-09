'use strict';

function loadHighscores() {
    fetch('http://127.0.0.1:5000/highscores')
        .then(response => response.json())
        .then(data => {
            const tbody = document.querySelector("#highscore_table tbody");
            tbody.innerHTML = "";
            data.forEach((entry, index) => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>${index + 1}</td>
                    <td>${entry.name}</td>
                    <td>${entry.points}</td>
                    <td>${entry.total_km.toFixed(1)}</td>
                    <td>${entry.total_co2.toFixed(3)}</td>
                `;
                tbody.appendChild(tr);
            });
        })
        .catch(err => console.error("Failed to load highscores:", err));
}
document.addEventListener("DOMContentLoaded", loadHighscores);