# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 15:53:55 2025

@author: eugenia
"""

import pandas as pd

# Load dataset (Make sure your CSV file is in the same folder as this script)
df = pd.read_csv("crop_rotation_data.csv")

# Display first few rows
print(df.columns)



# Check for missing values in recommended_crop
missing_count = df['recommended_crop'].isnull().sum()
print(f"Missing values before filling: {missing_count}")

# Define crop rotation rules
crop_rotation_rules = {
    'Maize': 'Pulses',  
    'Sugarcane': 'Wheat',
    'Wheat': 'Soybeans',
    'Tobacco': 'Maize',
    'Soybeans': 'Cotton',
    'Cotton': 'Ground Nuts',
    'Pulses': 'Barley',
    'Millet': 'Tobacco',
    'Barley': 'Sugarcane',
    'Oilseeds':'Millet',
    'Ground Nuts': 'Oilseeds'
    
    
}

# Fill recommended_crop based on previous_crop
df['recommended_crop'] = df['previous_crop'].map(crop_rotation_rules)

# Save updated dataset
df.to_csv("updated_crop_rotation_data.csv", index=False)

# Check missing values after filling
missing_count_after = df['recommended_crop'].isnull().sum()
print(f"Missing values after filling: {missing_count_after}")

# Show the first few rows
print(df.head())

# Remove rows where recommended_crop is missing
df_cleaned = df.dropna(subset=['recommended_crop'])

# Save the cleaned dataset
df_cleaned.to_csv("cleaned_crop_rotation_data.csv", index=False)

# Show number of rows removed
rows_removed = df.shape[0] - df_cleaned.shape[0]
print(f"Rows removed: {rows_removed}")
print(f"New dataset size: {df_cleaned.shape[0]} rows")

# Load dataset
df = pd.read_csv("crop_rotation_data.csv")

# Remove rows where recommended_crop is missing
df = df.dropna(subset=['recommended_crop'])

# Overwrite the original file
df.to_csv("crop_rotation_data.csv", index=False)

print("File successfully updated. Open 'crop_rotation_data.csv' in Excel to see changes!")

