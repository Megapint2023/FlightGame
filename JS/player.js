'use strict';

const gameState = {
  playerName: "",
  cash: 2500,
  points: 0,
  currentLocation: "Helsinki",
  icao: "",
  weather: "",
  totalDistance: 0,
  totalCO2: 0,
};

function updateStatusPanel() {
  document.getElementById("player_name").textContent = `PLAYER: ${gameState.playerName}`;
  document.getElementById("player_cash").textContent = `CASH: €${gameState.cash}`;
  document.getElementById("player_points").textContent = `POINTS: ${gameState.points}`;
  document.getElementById("player_location").textContent = `LOCATION: ${gameState.currentLocation}`;
  document.getElementById("player_location_icao").textContent = `ICAO: ${gameState.icao}`;
  document.getElementById("local_weather").textContent = `LOCAL WEATHER: ${gameState.weather}`;
  document.getElementById("total_distance_travelled").textContent = `TOTAL KM TRAVELLED: ${gameState.totalDistance}`;
  document.getElementById("total_CO2").textContent = `TOTAL CO2 CONSUMPTION: ${gameState.totalCO2}`;
}

window.addEventListener("DOMContentLoaded", () => {

  const modal = document.getElementById("player-modal");
  const form = document.getElementById("player-form");

  form.addEventListener("submit", (event) => {
    event.preventDefault();

    const nameInput = form.querySelector("input[type='text']");
    gameState.playerName = nameInput.value;

    // Hide the modal
    modal.style.display = "none";

    updateStatusPanel();
  });
});