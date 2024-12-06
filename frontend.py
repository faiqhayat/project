from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model (replace 'model.pkl' with your model file)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Prediction and index route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Get input data from request
            data = request.json
            if not data:
                return jsonify({"error": "No input data provided"}), 400

            # Extract features from input data
            humidity = float(data.get("humidity"))
            wind_speed = float(data.get("windSpeed"))

            # Prepare input for the model
            features = np.array([[humidity, wind_speed]])

            # Make prediction
            predicted_temp = model.predict(features)[0]

            # Return the prediction as JSON
            return jsonify({"temperature": round(predicted_temp, 2)})

        except Exception as e:
            return jsonify({"error": str(e)}), 400

    # Health check message for GET requests
    return jsonify({"message": "Send a POST request with 'humidity' and 'windSpeed' to get a temperature prediction."})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5000)
