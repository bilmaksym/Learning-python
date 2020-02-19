from sklearn.datasets import load_iris
import pandas as pd

pd.set_option('max_rows', 5)
import numpy as np

#reviews = pd.read_csv("../")

# Very useful describe method
#reviews.describe()
# OR
#reviews.points.describe()

# When you apply the map(function) method on a series, the map() function takes each element
# in the series and applies the function to it, and returns the transformed series.
# Here is example
data = load_iris()
features = pd.DataFrame(data=data['data'], columns=data[''])
print(features.head())

# example : let's say, we would like to change the measurement of the sepal length from cm to mm,
# this is what we can do with the map function and put a function call cm_to_mm inside.

def cm_to_mm(cm):
    mm = cm * 10
    return mm

print(features['sepal length (cm)'].map(cm_to_mm).head())

# With apply() we can fo the same but not only for one column but also to many by typing the colums, splitting by commas
