import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate random data for x
np.random.seed(42)
x = 2 * np.random.rand(100, 1)

# Generate corresponding y values with some noise
y = 2 * x + 1 + np.random.randn(100, 1)


# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# Get the model parameters
slope = model.coef_[0][0]
intercept = model.intercept_[0]

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")

# Make predictions
y_pred = model.predict(x)

# Plot the regression line
plt.scatter(x, y, label="Data")
plt.plot(x, y_pred, color='red', label="Regression Line")
plt.title("Linear Regression")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
