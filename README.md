House Price Prediction using Machine Learning
A Complete End-to-End Regression Project
📌 Overview

This project builds a machine-learning model to predict house sale prices based on multiple property features.
It includes data cleaning, exploratory data analysis (EDA), feature engineering, model training, and evaluation.

The code is written in Python using common data-science libraries and follows a clear, modular workflow.

📂 Project Structure
clean_house_price_project/
│
├── src/
│   └── house_price_prediction.py     # Main project script
│
├── data/
│   └── HousePriceData.xlsx           # (User-provided dataset)
│
├── requirements.txt                  # Dependencies
└── README.md                         # Project documentation

📑 Dataset Information

Place your dataset file inside:

data/HousePriceData.xlsx


The dataset should be an Excel file containing:

Essential Column

SalePrice — the target variable (numeric)

Example Feature Columns

Numerical: LotArea, GrLivArea, YearBuilt, TotalBsmtSF, GarageArea

Categorical: Neighborhood, HouseStyle, BuildingType, ExteriorMaterial

You may use:
✔ A dataset you created
✔ A publicly available housing dataset
✔ A modified/cleaned version of an existing dataset

The column names do not have to match these exactly — the script automatically handles categorical and numeric columns.

🧠 Project Workflow
1. Load Data

The script reads HousePriceData.xlsx from the data/ folder and verifies its structure.

2. Exploratory Data Analysis (EDA)

The script automatically generates:

A correlation heatmap of numerical features

A summary of categorical unique values

Visualizations saved as:

correlation_heatmap.png


These help in understanding:

Feature relationships

Potential multicollinearity

Data patterns and distributions

3. Data Preprocessing

Steps include:

Removing ID columns (if present)

Handling missing values

One-hot encoding categorical variables

Merging encoded features with numerical ones

Preparing clean training-ready data

4. Model Training

Three machine-learning regression models are implemented:

Support Vector Regression (SVR)

RandomForestRegressor

LinearRegression

Each model is trained on 80% of the data and tested on the remaining 20%.

5. Evaluation

The evaluation metric used:

MAPE — Mean Absolute Percentage Error

Advantages:

Easy to interpret

Measures prediction accuracy in percentage terms

Example output:

SVR: 0.123456
RandomForest: 0.085231
LinearRegression: 0.101987


Lower values mean better performance.

▶️ How to Run the Project
1. Install Dependencies
pip install -r requirements.txt

2. Add Your Dataset

Place the dataset file here:

data/HousePriceData.xlsx

3. Run the Script
python src/house_price_prediction.py

🧪 Requirements

The project uses the following Python libraries:

pandas
matplotlib
seaborn
scikit-learn
openpyxl


Make sure these are installed via requirements.txt.

🎯 Key Features

✔ Clean and modular code
✔ Automatic categorical encoding
✔ Multiple regression models
✔ Visual EDA outputs
✔ Easy to adapt for any housing dataset
✔ Excellent as an academic or portfolio project

📌 Notes

The dataset is not included in this project package — you must provide your own Excel file.

You may rename features or add additional ones; the script automatically adjusts.

The project is fully customizable — you can add scaling, hyperparameter tuning, or more models.

📜 License

This project is created for academic, learning, and portfolio purposes.
You are free to modify or extend it.python --version
