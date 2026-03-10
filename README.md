# 🏥 Smart Premium – Machine Learning Project

## 📌 Project Overview
This project predicts **insurance premium amounts** based on customer information using Machine Learning.

The system analyzes factors such as **age, income, health score, claim history, and policy details** to estimate the expected premium.

This project demonstrates a **complete Data Science workflow** including:

- Data Analysis
- Data Preprocessing
- Machine Learning Model Development
- Experiment Tracking with MLflow
- Model Deployment using Streamlit

---

# 📂 Project Structure

Insurance-Premium-Prediction
│
├── data
│ └── insurance_data.csv
│
├── notebooks
│ └── insurance_model_training.ipynb
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
└── mlruns


---

# 📊 Step 1: Understanding the Data

## 1.1 Load and Explore the Dataset

The dataset contains:

Customer Information
- Age
- Gender
- Annual Income
- Health Score
- Smoking Status
- Exercise Frequency

Policy Information
- Policy Type
- Region
- Claim History

Target Variable
- **Insurance Premium**

The dataset was loaded and analyzed to understand:
- Data structure
- Missing values
- Data distributions
- Feature relationships

---

## 1.2 Exploratory Data Analysis (EDA)

EDA was performed to identify patterns and trends in the data.

Analysis performed:
- Distribution plots
- Correlation analysis
- Outlier detection
- Feature relationship visualization

Libraries used:
- Matplotlib
- Seaborn

---

# ⚙️ Step 2: Data Preprocessing

Data preprocessing ensures that the dataset is clean and suitable for machine learning models.

## 2.1 Handling Missing Values

- Numerical columns → filled with **median values**
- Categorical columns → filled with **most frequent values (mode)**

---

## 2.2 Encoding Categorical Variables

Machine learning models require numerical input.

Categorical features such as:
- Gender
- Policy Type
- Region
- Smoking Status

were converted into numerical values using encoding techniques.

---

## 2.3 Train-Test Split

The dataset was divided into:

- **Training Data – 80%**
- **Testing Data – 20%**

Training data is used to train models, while testing data evaluates performance.

---

## 2.4 Feature Scaling

Feature scaling ensures all variables have similar ranges.

Scaling techniques used:
- StandardScaler
- Normalization

---

# 🤖 Step 3: Machine Learning Model Development

Since the goal is predicting a numerical value, **regression algorithms** were used.

Models trained:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

---

## Model Evaluation

Models were evaluated using:

- **R² Score**
- **RMSE (Root Mean Squared Error)**
- **MAE (Mean Absolute Error)**

The model with the **best performance metrics** was selected as the final model.

---

# 🔄 Step 4: ML Pipeline & MLflow Integration

## ML Pipeline

A pipeline was created to automate the workflow:

Data Preprocessing
↓
Model Training
↓
Model Evaluation
↓
Model Logging


---

## MLflow Experiment Tracking

MLflow was used to:

- Log model parameters
- Track evaluation metrics
- Compare multiple models
- Register trained models

MLflow stores:
- Experiment runs
- Model artifacts
- Model versions

---

# 🚀 Step 5: Model Deployment with Streamlit

The best-performing model was deployed using **Streamlit** to create an interactive web application.

## Application Features

Users can input customer details such as:

- Age
- Income
- Health Score
- Smoking Status
- Policy Type
- Region

The application processes the input and predicts the **estimated insurance premium**.

---

# 🖥️ Running the Project


---

##  Install Required Libraries



## 3️⃣ Run MLflow UI (Optional)
mlflow ui

http://localhost:5000

---

## 4️⃣ Run Streamlit App

http://localhost:8501


---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- MLflow
- Streamlit
- Matplotlib
- Seaborn

---

# 📈 Future Improvements

Possible improvements include:

- Hyperparameter tuning
- Feature engineering
- Deep learning models
- Cloud deployment (AWS / GCP)
- API deployment using FastAPI

---

# 👨‍💻 Author

**Rengaraj**

Data Science & Machine Learning Enthusiast

---

⭐ If you like this project, consider giving it a **star** on GitHub.
