import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load and preprocess the dataset
def load_data():
    df = pd.read_csv("processed_data.csv")
    X = df[["Humidity", "Wind Speed"]]
    y = df["Temperature"]
    return X, y

# Plot and log graphs to MLflow
def plot_and_log_graphs(X_train, y_train, y_pred):
    plt.figure(figsize=(8, 6))
    plt.scatter(y_train, y_pred, color="blue", label="Predicted vs Actual")
    plt.plot([y_train.min(), y_train.max()], [y_train.min(), y_train.max()], 'r--', label="Perfect Fit")
    plt.xlabel("Actual Temperature")
    plt.ylabel("Predicted Temperature")
    plt.title("Predicted vs Actual Temperature")
    plt.legend()
    plt.savefig("predicted_vs_actual.png")
    mlflow.log_artifact("predicted_vs_actual.png")

# Train the model and log to MLflow
def train_and_log():
    # Load data
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Enable MLflow autologging
    mlflow.set_experiment("Weather Prediction")
    
    with mlflow.start_run():
        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Log model
        mlflow.sklearn.log_model(model, "weather_model")

        # Log parameters
        mlflow.log_param("train_size", len(X_train))
        mlflow.log_param("test_size", len(X_test))

        # Log metrics
        mse = mean_squared_error(y_test, y_pred)
        mlflow.log_metric("mse", mse)

        # Plot and log graph
        plot_and_log_graphs(y_test, y_pred, y_pred)

        print(f"Run ID: {mlflow.active_run().info.run_id}")
        print("Model and metrics logged in MLflow.")

if __name__ == "__main__":
    train_and_log()
