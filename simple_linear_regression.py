#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:17:56 2019

@author: sghenimi
"""

import numpy
import matplotlib.pyplot as plot
import pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Import the dataset
dataset = pandas.read_csv('Salary_Data.csv')

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, 1]

# Split the dataset into the training set and test set
# splitting the data 30 rows: 20 rows for training set, 10 rows for testing set.
xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size = 1/3, random_state = 0)
linearRegressor = LinearRegression()
linearRegressor.fit(xTrain, yTrain)

yPrediction = linearRegressor.predict(xTest)

# Visualising the training set results
plot.scatter(xTrain, yTrain, color = 'red')
plot.plot(xTrain, linearRegressor.predict(xTrain), color = 'blue')
plot.title('Salary vs Experience (Training set)')
plot.xlabel('Years of Experience')
plot.ylabel('Salary')
plot.show()

# Visualising the test set results
plot.scatter(xTest, yTest, color = 'red')
plot.plot(xTrain, linearRegressor.predict(xTrain), color = 'blue')
plot.title('Salary vs Experience (Test set)')
plot.xlabel('Years of Experience')
plot.ylabel('Salary')
plot.show()

from sklearn.externals import joblib
joblib.dump(linearRegressor, "simple_linear_regression_model.pkl")
