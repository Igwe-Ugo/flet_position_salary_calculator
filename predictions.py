import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

dataset = pd.read_csv('Position_Salaries.csv')
pos = dataset.iloc[:, 0].values
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
print(pos)
print("========================")
print(y)

def predict_salaries(position):
    lin_reg = LinearRegression()
    poly_reg = PolynomialFeatures(degree=5)
    x_poly = poly_reg.fit_transform(x)
    lin_reg.fit(x_poly, y)
    result = lin_reg.predict(poly_reg.fit_transform([[position]]))
    return result

result = predict_salaries(7)
print(result)
