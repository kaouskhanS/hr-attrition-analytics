# 📊 HR Attrition Analytics & Prediction System

An end-to-end Machine Learning project that predicts employee attrition and provides interactive analytics through a Streamlit dashboard and FastAPI backend.

## 🚀 Project Overview

Employee attrition is one of the biggest challenges faced by organizations. This project uses Machine Learning to analyze employee data, identify factors influencing attrition, and predict whether an employee is likely to leave the company.

The application consists of:

- Data Generation
- Exploratory Data Analysis (EDA)
- Machine Learning Model Training
- FastAPI Prediction API
- Streamlit Dashboard

---

## ✨ Features

- 📈 Employee Attrition Prediction
- 📊 Interactive Analytics Dashboard
- 🤖 Machine Learning Classification Model
- 🔍 Exploratory Data Analysis (EDA)
- ⚡ FastAPI REST API
- 🎯 Attrition Probability Prediction
- 🐳 Docker Support

---

## 🛠️ Tech Stack

### Programming Language
- Python 3.x

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn
- Streamlit

### Backend
- FastAPI
- Uvicorn

### Deployment
- Docker

---

## 📁 Project Structure


hr-attrition-analytics-main/
│
├── analysis/
│   └── eda.py
│
├── backend/
│   └── app.py
│
├── dashboard/
│   └── streamlit_app.py
│
├── data/
│   └── generate_data.py
│
├── docker/
│   └── Dockerfile
│
├── model/
│   └── train_model.py
│
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/hr-attrition-analytics.git

cd hr-attrition-analytics
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Step 1: Generate Dataset

```bash
python data/generate_data.py
```

### Step 2: Perform Exploratory Data Analysis

```bash
python analysis/eda.py
```

### Step 3: Train the Machine Learning Model

```bash
python model/train_model.py
```

### Step 4: Start FastAPI Backend

```bash
uvicorn backend.app:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

### Step 5: Launch Streamlit Dashboard

```bash
streamlit run dashboard/streamlit_app.py
```

---

## 📊 Machine Learning Workflow

- Data Collection
- Data Preprocessing
- Exploratory Data Analysis
- Feature Engineering
- Model Training
- Model Evaluation
- Prediction API
- Dashboard Visualization

---

## 📈 Future Improvements

- Deploy on Render or Railway
- Connect to a real HR database
- Add Authentication
- Improve Model Accuracy
- Support Multiple ML Models
- Cloud Deployment

---

## 📸 Screenshots

Add screenshots of:

- Dashboard
- API Documentation
- Prediction Result
- Charts

---

## 📄 License

This project is intended for educational and portfolio purposes.

---

## 👨‍💻 Author

**Kaous Khan S**

B.Tech Artificial Intelligence and Data Science 

Mailam Engineering College

GitHub: https://github.com/your-username
LinkedIn: https://linkedin.com/in/your-profile
## Steps

1. Install dependencies:
pip install -r requirements.txt

2. Generate data:
python data/generate_data.py

3. Train model:
python model/train_model.py

4. Run API:
uvicorn backend.app:app --reload

5. Run dashboard:
streamlit run dashboard/streamlit_app.py
