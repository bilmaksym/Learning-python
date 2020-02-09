from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

# Load the data
data_path = "C/: ..."
data = pd.read_csv(data_path)

# Filter the data
filtered_data = data.dropna(axis=0)
# Choose targets and features
y = filtered_data.Price
data_features = ['Rooms', 'etc...']
X = data[data_features]

# Split data into training and validation data, for both features and target
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return (mae)

# Compare MAE with different values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: {} \t\t Mean Absolute Error: {}".format(max_leaf_nodes, my_mae))
