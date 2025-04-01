# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 14:12:48 2025

@author: eugenia
"""
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("crop_rotation_data.csv")

# Encode categorical columns
label_encoders = {}  # Dictionary to store all encoders
categorical_columns = ['previous_crop', 'soil_type']  # List of categorical columns

for col in categorical_columns:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col])  # Transform categorical values
    label_encoders[col] = encoder  # Store the encoder for later use

# Encode target variable (recommended_crop)
label_encoders['recommended_crop'] = LabelEncoder()  # Create and store the encoder
df['recommended_crop'] = label_encoders['recommended_crop'].fit_transform(df['recommended_crop'])  # Transform y

# Save all encoders, including recommended_crop
joblib.dump(label_encoders, "crop_label_encoder.pkl")

# Define features (X) and target (y)
X = df[['previous_crop', 'temperature', 'humidity', 'moisture', 'soil_type', 'soil_ph', 'rainfall']]
y = df['recommended_crop']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("✅ Model training successful!")

# Test model accuracy
y_pred = model.predict(X_test)
print(f"✅ Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# Save model
joblib.dump(model, "crop_rotation_model.pkl")
print("✅ Model saved successfully!")

# Load the saved model
model = joblib.load("crop_rotation_model.pkl")

# Load the LabelEncoder used during training
label_encoders = joblib.load("crop_label_encoder.pkl")

# Ensure 'recommended_crop' encoder exists before using it
if 'recommended_crop' not in label_encoders:
    raise ValueError("🚨 The label encoder for 'recommended_crop' was not found. Make sure you saved it during training.")

# Define feature names (must match training data)
feature_names = ['previous_crop', 'temperature', 'humidity', 'moisture', 'soil_type', 'soil_ph', 'rainfall']

# Example prediction (Ensure all 7 features are included)
sample_data = [[4, 35, 52, 28, 2, 10.5, 1000]]  # (Prev crop, Temp, Humidity, Moisture, Soil Type, Soil pH, Rainfall)

# Convert to DataFrame
sample_df = pd.DataFrame(sample_data, columns=feature_names)

# Predict crop (numeric label)
predicted_label = model.predict(sample_df)[0]

# Convert numeric prediction back to crop name
predicted_crop = label_encoders['recommended_crop'].inverse_transform([predicted_label])[0]

print(f"✅ Recommended Crop: {predicted_crop}")

import joblib
model = joblib.load("crop_rotation_model.pkl")
print("Model loaded successfully!")

