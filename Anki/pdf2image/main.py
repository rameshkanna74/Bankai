from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

app = Flask(__name__)

# Global objects
vectorizer = TfidfVectorizer()
scaler = StandardScaler()
knn = None

@app.route('/train', methods=['POST'])
def train_model():
    global vectorizer, scaler, knn

    # Get file path from the request
    file_path = request.json.get('file_path')
    if not file_path:
        return jsonify({"error": "File path is required"}), 400

    try:
        # Read the data
        df = pd.read_excel(file_path)

        # Ensure numeric column is clean
        df["matricule_ocr_value"] = pd.to_numeric(df["matricule_ocr_value"], errors='coerce')

        # Drop rows with invalid numeric values
        df = df.dropna(subset=["matricule_ocr_value"])

        # Extract features and target
        X_text = df["Full_name"]
        X_numeric = df["matricule_ocr_value"].values.reshape(-1, 1)
        y = df["Corrected_Name"]

        # Split the data into training and testing sets
        X_text_train, X_text_test, X_numeric_train, X_numeric_test, y_train, y_test = train_test_split(
            X_text, X_numeric, y, test_size=0.2, random_state=42
        )

        # Text feature vectorization
        X_text_train_vectors = vectorizer.fit_transform(X_text_train)
        X_text_test_vectors = vectorizer.transform(X_text_test)

        # Numeric feature scaling
        X_numeric_train_scaled = scaler.fit_transform(X_numeric_train)
        X_numeric_test_scaled = scaler.transform(X_numeric_test)

        # Combine text and numeric features
        X_train_combined = np.hstack([X_text_train_vectors.toarray(), X_numeric_train_scaled])
        X_test_combined = np.hstack([X_text_test_vectors.toarray(), X_numeric_test_scaled])

        # Train KNN model
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(X_train_combined, y_train)

        # Make predictions
        y_pred = knn.predict(X_test_combined)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        return jsonify({"message": "Model trained successfully", "accuracy": accuracy})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict', methods=['POST', 'GET'])
def predict_new_data():
    global vectorizer, scaler, knn

    if knn is None:
        return jsonify({"error": "Model is not trained yet. Please train the model first."}), 400

    try:
        # Get input data from the request
        matricule_number = request.json.get('matricule_number')
        full_name = request.json.get('full_name')

        if matricule_number is None or full_name is None:
            return jsonify({"error": "Both matricule_number and full_name are required."}), 400

        # Transform new text data using the existing vectorizer
        new_text_vectors = vectorizer.transform([full_name])

        # Scale new numeric data using the existing scaler
        new_numeric_scaled = scaler.transform(np.array([matricule_number]).reshape(-1, 1))

        # Combine new features
        new_combined = np.hstack([new_text_vectors.toarray(), new_numeric_scaled])

        # Predict using the trained KNN model
        prediction = knn.predict(new_combined)

        return jsonify({
            "matricule_number": matricule_number,
            "full_name": full_name,
            "predicted_name": prediction[0]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)