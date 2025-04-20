from flask import Flask, render_template, request
from dash import Dash, html, dcc, Input, Output
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('model/Attrition_Prediction.model')

# Job roles expected by the model (used for one-hot encoding)
job_roles = [
    'Research Scientist', 'Sales Executive', 'Laboratory Technician',
       'Sales Representative', 'Healthcare Representative',
       'Human Resources', 'Manufacturing Director', 'Manager',
       'Research Director'
        ]

@app.route('/')
def home():
    return render_template("home.html")  # Renders the form

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/prediction')  # NEW: This lets users visit the Prediction page
def prediction():
    return render_template('prediction.html')

@app.route('/how_to')
def how_to():
    return render_template('how_to.html')

# Prediction processing route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # 1. Get form values from prediction.html
        age = int(request.form['age'])
        overtime = request.form['overtime']  # "Yes" or "No"
        job_role = int(request.form['job_role'])
        job_level = int(request.form['job_level'])
        years_current_role = int(request.form['years_current_role'])
        job_involvement = int(request.form['job_involvement'])
        marital_status = int(request.form['marital_status'])
        satisfaction = int(request.form['satisfaction'])

        # 2. Convert to model-ready values
        overtime_val = 1 if overtime.lower() == 'yes' else 0

        # 3. One-hot encode job role
        job_role_vector = [1 if job_role == r else 0 for r in job_roles]

        # 4. Create DataFrame for prediction
        input_data = pd.DataFrame([[
            age,
            overtime_val,
            job_level,
            years_current_role,
            job_involvement,
            marital_status,
            satisfaction,
            job_role  # this is now just a number like 0-8
        ]], columns=[
            'Age', 'OverTime', 'JobLevel', 'YearsInCurrentRole',
            'JobInvolvement', 'MaritalStatus', 'JobSatisfaction', 'JobRole'
        ])


        # 5. Predict using model
        prediction = model.predict(input_data)[0]
        result = "Likely to Leave" if prediction == 1 else "Likely to Stay"

        return render_template("prediction.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
