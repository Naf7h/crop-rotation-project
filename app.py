from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("crop_rotation_model.pkl")

# Load label encoders
label_encoder = joblib.load("crop_label_encoder.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Extract features from request (ensure all 7 features are present)
        features = [[
            data["previous_crop"],
            data["temperature"],
            data["humidity"],
            data["moisture"],
            data["soil_type"],
            data["soil_ph"],
            data["rainfall"]
        ]]

        # Convert to DataFrame to match model input
        feature_names = ["previous_crop", "temperature", "humidity", "moisture", 
                         "soil_type", "soil_ph", "rainfall"]
        sample_df = pd.DataFrame(features, columns=feature_names)

        # Make prediction
        predicted_label = model.predict(sample_df)[0]

        # Convert numeric prediction back to actual crop name
        predicted_crop = label_encoder["recommended_crop"].inverse_transform([predicted_label])[0]

        return jsonify({"recommended_crop": predicted_crop})

    except Exception as e:
        return jsonify({"error": str(e)}), 400  # Return error message if something goes wrong

if __name__ == "__main__":
    app.run(debug=True)
