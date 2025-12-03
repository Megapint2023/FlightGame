async function updateWeather(cityName) {
  const apiKey = "YOUR_OPENWEATHERMAP_API_KEY";
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&units=metric&appid=${apiKey}`;

  try {
    const response = await fetch(url);
    const data = await response.json();
    const temp = data.main.temp;
    const description = data.weather[0].description;
    gameState.weather = `${temp}°C, ${description}`;

    // update panel
    document.getElementById("player-weather").textContent =
      `Weather: ${gameState.weather}`;
  } catch (err) {
    console.warn("Weather fetch failed:", err);
  }
}