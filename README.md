# 👥 Employee Attrition Prediction

This project provides a comprehensive machine learning solution for predicting and analyzing **employee attrition** (i.e., whether an employee will stay or leave).  
It aims to support HR professionals in making **data-driven retention decisions** and improving overall workforce stability.

## 🚀 Project Highlights

- Trained and evaluated **five machine learning models**:
  - Logistic Regression
  - Decision Tree Classifier
  - Random Forest Classifier
  - XGBoost Classifier (Gradient Descent)
  - LightGBM Classifier (Gradient Descent)

- ✅ **Best Performing Model**:  
  The **Gradient Descent LightGBM Classifier** achieved the highest prediction performance.

- 🔍 **Feature Importance Analysis** conducted using:
  - Algorithm-based feature importances
  - Permutation importance
  - SHAP (SHapley Additive exPlanations)

- 📊 Key influential features include:
  - OverTime
  - Job Level
  - Years in Current Role
  - Age
  - Job Role

---

## 📈 Visual Analytics

The project includes **graphical analysis** of attrition-related patterns to uncover underlying trends:
- Job Satisfaction vs Attrition
- Job Involvement vs Attrition
- Age Distribution vs Attrition

These visualizations help stakeholders better understand the behavioral and demographic drivers behind employee turnover.

---

## 🖥️ Web Application Overview

A user-friendly web interface was developed to help HR teams make **real-time attrition predictions**.

### 🏠 Home Page
- Provides an **overview of the importance of understanding employee attrition**
- Discusses the **business impact** of high turnover and the value of prediction tools

### 📊 Variables Page
- Explains the meaning of each input variable used in the prediction model
- Describes how each feature contributes to the likelihood of attrition

### 🤖 Attrition Prediction Page
- Allows users to **input employee attributes** (e.g., job level, overtime status, years in current role)
- Returns a **prediction** of whether the employee is likely to stay or leave

---

## 🧪 Dataset

- The dataset was sourced from **Kaggle** and additional open-source contributions on **GitHub**
- It includes anonymized records of employee data such as:
  - Age
  - Job Role
  - Job Satisfaction
  - Work Environment
  - Overtime
  - Tenure

No sensitive or personally identifiable information is used.

---

## 📁 How to Run the App

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Employees_Attrition_Prediction.git

2. **Run the app**
   ```bash
   python app.py

3. **Access the app**
   ```bash
   http://localhost:5000



