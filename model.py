import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load data
data = pd.read_csv("processed_data.csv")

# Split features and target
X = data[["Humidity", "Wind Speed"]]
y = data["Temperature"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved to model.pkl")
