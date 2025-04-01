<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Farmer Dashboard</title>
    <link rel="stylesheet" href="styles.css">
    <script defer src="script.js"></script>
</head>
<body>
    <div class="dashboard-container">
        <header>
            <h1>Welcome, Farmer!</h1>
            <p>Your crop rotation recommendations and farm updates.</p>
        </header>
        
        <section class="summary">
            <div class="card" id="crop-suggestion">
                <h2>Next Crop Suggestion</h2>
                <p id="suggested-crop">Loading...</p>
            </div>
            
            <div class="card" id="weather-update">
                <h2>Weather Update</h2>
                <p id="weather-info">Fetching data...</p>
            </div>
        </section>
        
        <section class="navigation">
            <a href="#" class="btn">View Detailed Analysis</a>
            <a href="#" class="btn">Manage Your Farm</a>
            <a href="#" class="btn">Settings</a>
            <a href="#" class="btn">Logout</a>
        </section>
    </div>
</body>
</html>




//farmer dashboard
// Mock crop rotation suggestions
const cropSuggestions = [
    { season: "Spring", crop: "Corn", soil: "Loamy", benefits: "Improves soil nitrogen levels" },
    { season: "Summer", crop: "Soybeans", soil: "Clay", benefits: "Fixes nitrogen and improves soil health" },
    { season: "Fall", crop: "Wheat", soil: "Sandy", benefits: "Prepares soil for legumes" },
    { season: "Winter", crop: "Clover", soil: "Silty", benefits: "Adds organic matter to the soil" }
];

// Display crop recommendations
function loadCropRecommendations() {
    const cropContainer = document.getElementById("crop-suggestions");
    cropContainer.innerHTML = "";

    cropSuggestions.forEach(suggestion => {
        let cropCard = document.createElement("div");
        cropCard.classList.add("card");
        cropCard.innerHTML = `
            <h3>${suggestion.season} Planting</h3>
            <p><strong>Crop:</strong> ${suggestion.crop}</p>
            <p><strong>Best Soil Type:</strong> ${suggestion.soil}</p>
            <p><strong>Benefits:</strong> ${suggestion.benefits}</p>
        `;
        cropContainer.appendChild(cropCard);
    });
}

// Fetch weather data (Mock API)
function fetchWeather() {
    const weatherContainer = document.getElementById("weather-info");
    const weatherAPI = `https://api.open-meteo.com/v1/forecast?latitude=34.05&longitude=-118.25&current_weather=true`;

    fetch(weatherAPI)
        .then(response => response.json())
        .then(data => {
            let weather = data.current_weather;
            weatherContainer.innerHTML = `
                <div class="card">
                    <h3>Current Weather</h3>
                    <p><strong>Temperature:</strong> ${weather.temperature}°C</p>
                    <p><strong>Wind Speed:</strong> ${weather.windspeed} km/h</p>
                    <p><strong>Conditions:</strong> ${weather.weathercode}</p>
                </div>
            `;
        })
        .catch(error => {
            weatherContainer.innerHTML = `<p style="color: red;">Failed to fetch weather data.</p>`;
        });
}

// Load data when the page loads
document.addEventListener("DOMContentLoaded", () => {
    loadCropRecommendations();
    fetchWeather();
});
