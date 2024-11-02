
from sklearn.linear_model import LinearRegression
import numpy as np

# Example model training
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3
model = LinearRegression().fit(X, y)

def predict(input_data):
  return model.predict(input_data)

