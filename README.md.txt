# 🚗 Car Price Prediction using Machine Learning

A Machine Learning project that predicts the estimated selling price of a used car based on its details.

## 📌 Project Overview

This project uses a **Random Forest Regressor** to predict used car selling prices.

The model takes the following information as input:

- Manufacturing Year
- Present Price
- Kilometers Driven
- Previous Owners
- Fuel Type
- Seller Type
- Transmission

A **Streamlit web application** was developed to allow users to enter car details and get a predicted selling price.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib
- Jupyter Notebook

## 🤖 Machine Learning Model

**Algorithm:** Random Forest Regressor

The dataset was divided into:

- 80% Training Data
- 20% Testing Data

### Model Evaluation

- MAE: 0.96
- RMSE: 1.26
- R² Score: 0.80

> Note: The current project uses a small dataset of 30 records, so these evaluation results should be considered for demonstration purposes rather than as a measure of real-world performance.

## 📊 Dataset Features

| Feature | Description |
|---|---|
| Year | Manufacturing year of the car |
| Present_Price | Current price of the car |
| Kms_Driven | Kilometers driven |
| Owner | Number of previous owners |
| Fuel_Type | Petrol or Diesel |
| Seller_Type | Dealer or Individual |
| Transmission | Manual or Automatic |
| Selling_Price | Target selling price |

## 🌐 Streamlit Web App

The project includes an interactive web application where users can:

1. Enter car information
2. Select vehicle details
3. Predict the estimated selling price
4. Compare the current market price with the predicted price

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL