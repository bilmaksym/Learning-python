import pandas as pd

reviews = pd.read_csv("../", index_col=0)
pd.set_option('max_rows', 5)

# We can also change the index that we setup earlier
reviews.set_index()

# We use operators loc and iloc when accessing by indexes
# Loc is label-based and iloc is index_based
# For example
temp = reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]

