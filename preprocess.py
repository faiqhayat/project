import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load raw data
data = pd.read_csv("raw_data.csv")

# Handle missing values
data = data.fillna(method='ffill')

# Normalize numerical fields
scaler = MinMaxScaler()
data[["Temperature", "Wind Speed"]] = scaler.fit_transform(data[["Temperature", "Wind Speed"]])

# Save preprocessed data
data.to_csv("processed_data.csv", index=False)
print("Preprocessed data saved to processed_data.csv")
    