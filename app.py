from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)

# Load saved model and objects
model = joblib.load('employee_attrition_dataset.joblib')
feature_columns = joblib.load('feature_columns.joblib')
le = joblib.load('label_encoder.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.form.to_dict()
        
        # Create DataFrame
        input_df = pd.DataFrame([data])
        
        # Convert numeric columns
        numeric_cols = ['Age', 'Job_Level', 'Monthly_Income', 'Hourly_Rate', 
                       'Years_at_Company', 'Years_in_Current_Role', 
                       'Years_Since_Last_Promotion', 'Work_Life_Balance',
                       'Job_Satisfaction', 'Performance_Rating', 
                       'Training_Hours_Last_Year', 'Project_Count',
                       'Average_Hours_Worked_Per_Week', 'Absenteeism',
                       'Work_Environment_Satisfaction', 'Relationship_with_Manager',
                       'Job_Involvement', 'Distance_From_Home', 
                       'Number_of_Companies_Worked']
        
        for col in numeric_cols:
            if col in input_df.columns:
                input_df[col] = pd.to_numeric(input_df[col])
        
        # One-hot encoding (same as training)
        categorical_cols = ['Gender', 'Marital_Status', 'Department', 'Job_Role', 'Overtime']
        input_df = pd.get_dummies(input_df, columns=categorical_cols, drop_first=True)
        
        # Align columns with training features
        for col in feature_columns:
            if col not in input_df.columns:
                input_df[col] = 0
        
        input_df = input_df[feature_columns]  # Keep only training columns in correct order
        
        # Make prediction
        probability = model.predict_proba(input_df)[0][1]
        prediction = "Yes (Likely to Leave)" if probability > 0.5 else "No (Likely to Stay)"
        
        return render_template('index.html', 
                               prediction=prediction, 
                               probability=round(probability * 100, 2))
    
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)