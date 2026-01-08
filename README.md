# Placement Score Predictor

The Placement Score Predictor is a Machine Learning–based application designed to estimate a student’s placement readiness score using key academic and skill-based parameters. The project aims to provide a data-driven assessment that helps students understand their current standing and identify areas for improvement.

---

## Project Overview

This project uses a regression-based machine learning model trained on structured data to predict a placement readiness score on a scale of 0–100. The prediction is based on factors such as CGPA, technical skill level, and domain knowledge. The application demonstrates the complete ML workflow, from data preprocessing and model training to deployment-ready integration.

---

## Features

- Predicts placement readiness score (0–100)
- Uses a trained and serialized machine learning model
- Accepts multiple academic and skill-based inputs
- Clean and user-friendly interface
- Real-time prediction based on user input
- Suitable for academic projects and placement analysis

---

## Machine Learning Details

- **Model Type:** Regression model  
- **Training Approach:** Supervised learning on structured data  
- **Input Parameters:**
  - CGPA (0–10)
  - Technical Skills Score (0–10)
  - Domain Knowledge Score (0–10)
- **Output:**
  - Placement Readiness Score (0–100)

The model is trained offline and saved using Pickle for reuse during inference.

---

## Technology Stack

- Python
- Machine Learning (scikit-learn)
- HTML, CSS, JavaScript (Frontend)
- Git & GitHub (Version Control)

---

## Project Structure

