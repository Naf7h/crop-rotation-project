// Crop rotation recommendations based on soil type and previous crop
const cropRotationData = {
    "Loamy": { "Corn": "Soybeans", "Soybeans": "Wheat", "Wheat": "Clover" },
    "Clay": { "Rice": "Barley", "Barley": "Peas", "Peas": "Oats" },
    "Sandy": { "Carrots": "Lettuce", "Lettuce": "Tomatoes", "Tomatoes": "Onions" },
    "Silty": { "Potatoes": "Beans", "Beans": "Maize", "Maize": "Alfalfa" }
};

// Handle form submission
document.getElementById("crop-form").addEventListener("submit", function (event) {
    event.preventDefault();

    let soilType = document.getElementById("soil-type").value;
    let previousCrop = document.getElementById("previous-crop").value;
    let recommendationsDiv = document.getElementById("recommendations");

    let nextCrop = cropRotationData[soilType]?.[previousCrop];

    recommendationsDiv.innerHTML = nextCrop
        ? `<div class="card"><h3>Recommended Crop</h3><p>Next Best Crop: <strong>${nextCrop}</strong></p></div>`
        : `<p style="color: red;">No recommendation found. Try another crop.</p>`;
});
