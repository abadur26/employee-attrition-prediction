# Employee Attrition Prediction

A complete **Machine Learning** web application that predicts whether an employee is likely to leave the company (attrition) using **Logistic Regression**.

The project includes data analysis, model training, and a clean interactive web interface built with **Flask**.
![employee_attrition_Prediction](https://github.com/user-attachments/assets/1291655f-745e-4677-b3ba-ade70a9085ea)
*(Replace with actual screenshot of your deployed app or the form you have)*

## 🎯 Problem Statement
Employee attrition is a major challenge for organizations. This project helps HR teams identify employees at high risk of leaving by analyzing factors like age, income, job role, overtime, etc.

## ✨ Features
- Interactive web-based prediction form (2-column modern UI)
- Trained Logistic Regression model
- Data exploration and visualizations (EDA)
- Model evaluation and feature analysis
- Clean, responsive Glassmorphism design
- Reset and Predict functionality

## 📁 Project Structure
employee-attrition-prediction/
├── app.py                          # Flask web application
├── templates/
│   └── index.html                  # Frontend form (updated two-column design)
├── employee_attrition_on_dataset.csv   # Original dataset
├── employee_attrition_on_dataset_1000.csv
├── data_processes.ipynb            # Data processing & EDA
├── logistic_attrition_model.joblib # Trained model
├── label_encoder.joblib            # Label encoders
├── scaler.joblib                   # Feature scaler
├── feature_columns.joblib
├── *.png                           # Visualizations (age distribution, correlation heatmap, etc.)
└── README.md

## 🛠️ Technologies Used
- **Python**
- **Flask** — Web framework
- **Scikit-learn** — Machine Learning (Logistic Regression)
- **Pandas & NumPy** — Data manipulation
- **Joblib** — Model & encoder saving
- **HTML, CSS, Jinja2** — Frontend
- **Matplotlib & Seaborn** — Visualizations

## 🚀 How to Run Locally

### Prerequisites
- Python 3.8 or higher

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/employee-attrition-prediction.git
   cd employee-attrition-prediction

2. **Create and activate virtual environment (Recommended)**
   python -m venv venv
  # Windows
  venv\Scripts\activate
  # macOS / Linux
  source venv/bin/activate
  
3. **Install dependencies**
    pip install flask pandas numpy scikit-learn joblib

4. **Run the application**
   python app.py
5. Open your browser and go to: http://127.0.0.1:5000/



📊 Model & Insights

Algorithm: Logistic Regression
Includes preprocessing: Label Encoding + Standard Scaling
Key influencing factors: Overtime, Monthly Income, Age, Years at Company, etc.
Visualizations included for better understanding of data patterns.

📸 Screenshots
(Add screenshots here later)

Web Interface
Correlation Heatmap
Attrition by Department
Age Distribution

🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.
📄 License
This project is open-source and available under the MIT License.
👨‍💻 Author
Abadur
Made with ❤️ for HR Analytics & Machine Learning enthusiasts.

Star this repository if you found it helpful! ⭐


### 5. Additional Tips for Creating the Repository

1. **Create the repo on GitHub**:
   - Go to [github.com/new](https://github.com/new)
   - Repository name: `employee-attrition-prediction`
   - Description: Paste the one I gave above
   - Public (recommended for portfolio)
   - Add a README file → **Uncheck** this (we will add our own)
   - Create repository

2. **After creating**:
   - Upload all your files (including the improved `index.html`)
   - Add the `README.md` file
   - Add a nice screenshot of your web form as the repository image (optional but recommended)

3. **.gitignore** (Create this file too)
   Create a file named `.gitignore` with this content:
     pycache/
    venv/
    *.pyc
    .env
    *.log

   
Would you like me to also write:
- A good `.gitignore` with more details?
- Requirements.txt content?
- License file (MIT)?
- Instructions to deploy on Render / Railway / Heroku?

Just say **"yes"** or tell me what else you need. You're ready to push this to GitHub now! 🚀
