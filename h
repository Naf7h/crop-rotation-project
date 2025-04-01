document.getElementById("crop-form").addEventListener("submit", function(event) {
    event.preventDefault();

    let previousCrop = document.getElementById("previous-crop").value;
    let soilPH = parseFloat(document.getElementById("soil-ph").value);
    let soilType = document.getElementById("soil-type").value;
    let rainfall = parseInt(document.getElementById("rainfall").value);
    let temperature = parseInt(document.getElementById("temperature").value);
    

    // Simulated AI logic (Replace with actual ML model)
    let recommendedCrop = getCropSuggestion(previousCrop, soilPH, soilType, rainfall, temperature);

    document.getElementById("ai-suggestion").innerText = "Recommended Crop: " + recommendedCrop;
});

// AI Crop Rotation Logic (Replace with an actual ML model)
function getCropSuggestion(previousCrop, soilPH, soilType, rainfall, temperature) {
    if (previousCrop === "Wheat") {
        if (soilPH > 6.5 && rainfall > 800) {
            return "Soybeans";
        } else {
            return "Maize";
        }
    } else if (previousCrop === "Maize") {
        return soilType === "Loamy" ? "Wheat" : "Millet";
    } else if (previousCrop === "Millet") {
        return temperature < 25 ? "Barley" : "Soybeans";
    } else if (previousCrop === "Soybeans") {
        return rainfall > 1000 ? "Millet" : "Tobacco";
    } else {
        return "Wheat";  // Default suggestion
    }
}
