# Real-Estate-Prediction
This project aims to predict housing prices based on various features using a Decision Tree Regressor. By analyzing real estate data, we can provide price estimates for houses based on input parameters such as bedroom ratio, population level, and median income.

## Tools and Technologies
Pandas: For data manipulation and analysis.

NumPy: For numerical computations.

Scikit-learn: For implementing the Decision Tree Regressor.

Flask: For creating the web application.

Matplotlib & Seaborn: For creating visualizations during the data exploration phase.

## Project Overview
### i) Data Preprocessing
Loading the housing data from housing.csv.

Handling missing values by dropping rows with missing data.

Applying log transformations to skewed features like total_rooms, total_bedrooms, population, and households.

Converting categorical feature (ocean_proximity) to binary using one-hot encoding.

### ii) Data Exploration
Splitting the data into training and testing sets.

Plotting histograms to visualize the distribution of various features.

Using heatmaps to visualize correlations between features and the target variable (median_house_value).

Applying log transformations to reduce skewness in features.

### iii) Feature Engineering
Creating new features such as bedroom_ratio (total_bedrooms / total_rooms) and household_rooms (total_rooms / households).

### iv) Model Training
Training a Decision Tree Regressor on the preprocessed data.

### v) Web Application
Creating a Flask web application with an input form to collect user inputs.

Making predictions based on user inputs and displaying the predicted house price.

## Installation and Usage
### Prerequisites
Python 3.x
Required Python libraries: pandas, numpy, scikit-learn, flask, matplotlib, seaborn

Installation
### Clone the repository and navigate to the project directory:
bash

cd Real-Estate-Price-Prediction

### Start the Flask web server:
bash

python app.py

Open a web browser and go to http address to access the application.

Enter the required input parameters and submit the form to get the predicted house price.


## Future Enhancements
Implement additional machine learning models for improved predictions.

Enhance the web application with more interactive features and visualizations.

Integrate more detailed data for better model accuracy.

The model might be prone to overfitiing, investigate the use of L1 or L2 regularization.

![image](https://github.com/user-attachments/assets/80f47c44-fb1d-4eff-acdb-c8152de84328)
![image](https://github.com/user-attachments/assets/62e5f177-1a29-4996-959b-86521caaffda)


![image](https://github.com/user-attachments/assets/0cc90aaa-9a15-41c4-a075-31e8db5a0922)
skewed graph:
![image](https://github.com/user-attachments/assets/28d4083f-df5d-424d-91df-563993920a3f)
corrected graph:
![image](https://github.com/user-attachments/assets/006e9a7c-7896-4c11-a235-26b7e4cdef0b)
Blue is less expensive, consider the blank sector below red as the ocean:
![image](https://github.com/user-attachments/assets/e0cf1227-79af-4188-ba0f-18dba18368f1)
Heatmap after combining bedroom features:
![image](https://github.com/user-attachments/assets/a02b2fee-6f47-4030-9b21-0829863b042f)


