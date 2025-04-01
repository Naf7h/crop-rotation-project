document.getElementById("crop-form").addEventListener("submit", async function (event) {
    event.preventDefault();

    let previous_crop = document.getElementById("previous-crop").value;
    let temperature = parseInt(document.getElementById("temperature").value);
    let humidity = parseInt(document.getElementById("humidity").value);
    let moisture = parseInt(document.getElementById("moisture").value);
    let soil_type = document.getElementById("soil-type").value;
    let soil_ph = parseFloat(document.getElementById("soil-ph").value);
    let rainfall = parseInt(document.getElementById("rainfall").value);
    

    let requestData = {
        previous_crop: previous_crop,
        temperature: temperature,
        humidity: humidity,
        moisture: moisture,
        soil_type: soil_type,
        soil_ph: soil_ph,
        rainfall: rainfall
        
    };

    try {
        let response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestData)
        });

        let result = await response.json();
        document.getElementById("ai-suggestion").textContent = `Recommended Crop: ${result.recommended_crop}`;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("ai-suggestion").textContent = "Error fetching prediction.";
    }
});
