import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Load the data
melbourne_filepath = "C/: ..."
melbourne_data = pd.read_csv(melbourne_filepath)

# Filter rows with missing price values
filtred_melbourne_data = melbourne_data.dropna(axis=0)
# Choose target and features
y = filtred_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = filtred_melbourne_data[melbourne_features]

# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(X, y)

# Once we have a model here is how we calculate mean absolute error
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)

# Let's split our data in two pieces: training data and validation data, for both features and target
from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))

