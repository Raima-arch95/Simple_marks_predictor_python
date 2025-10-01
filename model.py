import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

dataset = pd.read_csv("marks - Sheet1.csv")
y = dataset['marks']
x = dataset['hrs']
X = x.values.reshape(-1,1)

model = LinearRegression()
model.fit(X ,  y)

joblib.dump(model , "mymarksmodel")
