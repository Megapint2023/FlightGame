'use strict';

const name = {
  player_name: "",
};

function update_player_name() {
  document.getElementById("player_name").textContent = name.player_name;
}
function update_stats(data) {
    document.getElementById("player_cash").textContent = data.cash + " €";
    document.getElementById("player_points").textContent = data.points;
    document.getElementById("player_location").textContent = data.location;
    document.getElementById("player_sijainti").textContent = data.location;
    document.getElementById("player_location_icao").textContent = data.icao;
    document.getElementById("total_distance").textContent = data.total_distance.toFixed(1) + " km";
    document.getElementById("total_CO2").textContent = data.total_consumption.toFixed(1) + " t";
    document.getElementById("player_country").textContent = data.country;
}

window.addEventListener("DOMContentLoaded", () => {

  const modal = document.getElementById("player-modal");
  const form = document.getElementById("player-form");

  form.addEventListener("submit", (event) => {
    event.preventDefault();

    const nameInput = form.querySelector("input[type='text']");
    name.player_name = nameInput.value;

    modal.style.display = "none";

    update_player_name();
  });
});