# RetailIQ - AI Retail Analytics

## Project Overview

RetailIQ is an AI-powered retail analytics project that helps small businesses analyze sales performance, understand customer buying patterns, and make data-driven decisions.

The project combines **Data Analytics, Machine Learning, Power BI Visualization, and Streamlit Deployment** to provide sales insights and revenue prediction.

---

## Problem Statement

Small retail businesses often store sales records without proper analysis, making it difficult to identify sales trends, profitable products, and future revenue opportunities.

RetailIQ solves this problem by analyzing historical sales data and providing:

* Sales insights
* Profit analysis
* Product performance analysis
* Revenue prediction

---

##  Features

### Data Analysis

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Revenue and profit calculation
* Sales trend analysis

###  Machine Learning Prediction

* Predicts future revenue based on sales data
* Trained Machine Learning model
* Model saved using Pickle (.pkl)

###  Power BI Dashboard

* Interactive sales dashboard
* Revenue analysis
* Profit analysis
* Product and category performance insights

###  Streamlit Web Application

* User-friendly interface
* Real-time prediction
* Interactive visualization
* Deployed online for easy access

---

##  Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib / Pickle
* Matplotlib
* Streamlit
* Power BI
* Google Colab
* GitHub

---

##  Machine Learning Model

Algorithm Used:

**Random Forest Regression**

The model was trained using cleaned retail sales data to predict revenue based on input features.

Model File:

`retail_sales_model.pkl`

Evaluation metrics used:

* Mean Absolute Error (MAE)
* Root Mean Square Error (RMSE)
* R² Score

---

##  Dataset Description

The dataset contains retail store sales information including:

| Column        | Description              |
| ------------- | ------------------------ |
| Date          | Sales transaction date   |
| Product_Name  | Name of product          |
| Category      | Product category         |
| Brand         | Product brand            |
| Quantity      | Number of items sold     |
| Selling_Price | Selling price of product |
| Cost_Price    | Cost price of product    |
| Revenue       | Total sales revenue      |
| Profit        | Generated profit         |

---

##  Power BI Dashboard

The Power BI dashboard provides insights into:

* Total Revenue
* Total Profit
* Product performance
* Category-wise sales
* Monthly sales trends
* Business performance analysis

Dashboard File:

`PowerBI_Dashboard.pbix`

---

##  Streamlit Application

The Streamlit application allows users to interact with the trained ML model and generate revenue predictions.

Live Application:

https://retailiq-ai-retail-analytics-fdvbt8pxlpvfhrosubbwb7.streamlit.app/

---

##  Screenshots

Screenshots include:

* Streamlit Home Page
* Prediction Page
* Revenue Prediction Result
* Profit Analysis
* Power BI Dashboard
* Data Visualization Charts

---

##  Project Structure

```
RetailIQ-AI-Retail-Analytics

│
├── RetailIQ_Streamlit_App
│   ├── app.py
│   ├── requirements.txt
│   ├── retail_sales_model.pkl
│   └── Retailstores_Cleaned.csv
│
├── data
│
├── notebooks
│   └── RetailIQ_ML_Model.ipynb
│
├── reports
│   └── PowerBI_Dashboard.pbix
│
├── Screenshots
│
├── README.md
└── requirements.txt
```

---

## 🔗 GitHub Repository

https://github.com/jeniferrajamuthu2k7-maker/RetailIQ-AI-Retail-Analytics

---

## Future Enhancements

* Real-time inventory management
* Customer purchase prediction
* Sales forecasting using advanced ML models
* Cloud database integration
* Mobile application development

---

## Author

**Jenifer R**
BSc Artificial Intelligence and Machine Learning
