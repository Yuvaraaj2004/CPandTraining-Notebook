#import required libraries
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error
  
#Step 1 : Load the dataset


#Step 2 : Shape or Dimensions of the DataFrame
print("DF Shape")

print()

#Step 3 : Explore Data Types of the various columns
print("DF Column Types")

print()


#Step 4 : Reindex data using a Datetime Index

#Step 5 : Explore data by displaying 5 rows
print("Top 5 rows")

print()

#Step 6 : Printing Statistical Summary of the dataset
print("Statistical Summary")

print()
#Step 7 :  Checking for empty data fields in the dataset
print("Columns and null values")

print()

#Step 8: Split dataset in features and target variable

#Step 9 : Split dataset into training set and test set (30% test data size)

#Step 10 : Create the Linear Regression model 

#Step 11 : Train the Linear Regression Model

#Step 12 : Predict the response for test dataset

#Step 13 : Create a new DataFrame with the Actual Price and Predicted Price for the test dataset
#Print the first 20 values
print("First 20 values")

print()

#Step 14 : Generate line plots for Actual Price and Predicted Price using sns.lineplot
#Plot Title : Regression Analysis, xlabel : Date, ylabel : Actual/Predicted Price, Title : Regression Analysis

plt.suptitle("Regression Analysis")
plt.xlabel("Date")
plt.ylabel("Actual/Predicted Price")
plt.savefig("Regression.jpg")

#Step 15 : Check the accuracy of the Linear Regression Model
print("Linear Regression Score")

print()

#Step 16 : Print intercepts and coefficients
print("Intercept")

print("Coefficients")

print()

#Step 17 : Print Regression Evaluation Metrics
print("MAE")

print("MSE")

print("RMSE:")






