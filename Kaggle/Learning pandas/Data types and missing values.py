import pandas as pd
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('max_rows', 5)

# Grab the type of a specific column(series)
result = reviews.price.dtype

# Or the every column in DataFrame
result_all = reviews.dtype

# It is possible to convert type of the column to another by using the following expression
reviews.points.astype("float64")

# To select NaN entries you can use pd.isnull() (or its companion pd.notnull()).
nan_values = reviews[pd.isnull(reviews.country)]

# Pandas provides a really handy method for this problem: fillna(). This function replaces NaN with value that you choose.
replaced = reviews.region_2.fillna("Unknown")

# Sometimes it is very handy to use a replace method in cases, when data has changed
changed = reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")
