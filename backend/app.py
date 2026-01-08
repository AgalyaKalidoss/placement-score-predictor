from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

with open("placement_model.pkl", "rb") as f:
    model = pickle.load(f)

def clamp(x, lo=0, hi=100):
    return max(lo, min(hi, x))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    try:
        cgpa = float(data["cgpa"])
        tech = int(data["tech_skills"])
        domain = int(data["domain_knowledge"])
        intern = int(data["internships"])
    except:
        return jsonify({"error": "Invalid input format"}), 400

    # -------------------------------
    # HARD FAIL CONDITIONS (CRITICAL)
    # -------------------------------
    if cgpa < 6.0:
        return jsonify({
            "placement_score": 25,
            "status": "Very Low",
            "advice": "CGPA below minimum requirement"
        })

    if tech < 3 or domain < 3:
        return jsonify({
            "placement_score": 30,
            "status": "Very Low",
            "advice": "Core skills too weak for placement"
        })

    # -------------------------------
    # ML PREDICTION
    # -------------------------------
    features = np.array([[cgpa, tech, domain, intern]])
    ml_score = model.predict(features)[0]

    # -------------------------------
    # RULE-BASED ADJUSTMENTS
    # -------------------------------
    penalty = 0
    bonus = 0

    if tech < 6:
        penalty += 10
    if domain < 6:
        penalty += 8
    if intern == 0:
        penalty += 5

    if cgpa >= 8.5:
        bonus += 5
    if tech >= 8:
        bonus += 7
    if domain >= 8:
        bonus += 5
    if intern >= 2:
        bonus += 5

    final_score = clamp(ml_score - penalty + bonus)

    # -------------------------------
    # STATUS
    # -------------------------------
    if final_score >= 80:
        status = "High"
        advice = "Strong placement readiness"
    elif final_score >= 60:
        status = "Moderate"
        advice = "Improve skills to boost chances"
    else:
        status = "Low"
        advice = "Needs significant improvement"

    return jsonify({
        "placement_score": round(final_score, 2),
        "status": status,
        "advice": advice
    })

if __name__ == "__main__":
    app.run(debug=True)
