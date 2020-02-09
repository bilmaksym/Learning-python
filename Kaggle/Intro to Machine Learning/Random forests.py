import pandas as pd

# Load the data
data_path = "C/: ..."
data = pd.read_csv(data_path)

# Filter rows with missing values
data.dropna(axis=0)
# Choose target and features
y = data.Price
data_features = ['Rooms', 'etc...']
X = data[data_features]

from sklearn.model_selection import train_test_split
train_X, train_y, val_X, val_y = train_test_split(X, y, random_state=0)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
data_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, data_preds))
