import pandas as pd
from sklearn.model_selection import train_test_split as split

# Read the data
data = pd.read_csv('../')

# Select subset of predictors
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]

# Select target
y = data.Price

# Separate data into training and validation sets
X_train, X_valid, y_train, y_valid = split(X, y)

from xgboost import XGBRegressor

my_model = XGBRegressor()
my_model.fit(X_train, y_train)

from sklearn.metrics import mean_absolute_error

predictions = my_model.predict(X_valid)
print("Mean Absolute4 Error: " + str(mean_absolute_error(predictions, y_valid)))

# Set the number of the ensembles
my_model = XGBRegressor(n_estimators=500)
my_model.fit(X_train, y_train)

# Set up early_stopping_rounds which can help us to find the best value for n_estimators
my_model = XGBRegressor(n_estimators=500)
my_model.fit(X_train, y_train,
             early_stopping_rounds=5,
             eval_set=[(X_valid, y_valid)],
             verbose=False)

# In general, a small learning rate and large number of estimators will yield more accurate XGBoost models,
# though it will also take the model longer to train since it does more iterations through the cycle.
# As default, XGBoost sets learning_rate=0.1.
my_model = XGBRegressor(n_estimators=1000, learning_rate=0.05)
my_model.fit(X_train, y_train,
             early_stopping_rounds=5,
             eval_set=[(X_valid, y_valid)],
             verbose=False)

# Also we can set up number of jobs to increase speed of modeling on larger datasets, that parameter would just create a number of streams
# It's common to set the parameter n_jobs equal to the number of cores on your machine.
my_model = XGBRegressor(n_estimators=1000, learning_rate=0.05, n_jobs=4)
my_model.fit(X_train, y_train,
             early_stopping_rounds=5,
             eval_set=[(X_valid, y_valid)],
             verbose=False)

