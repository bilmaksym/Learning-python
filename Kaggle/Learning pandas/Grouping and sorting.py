import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# For example we want to get the cheapest wine in each point value category
reviews.groupby('points').price.min()

# Here's one way of selecting the name of the first wine reviewed from each winery in the dataset:
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])

# We can also group by more than one column
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])

# Another groupby() method worth mentioning is agg(), which lets you run a bunch of different functions on your
# DataFrame simultaneously.
# For example, we can generate a simple statistical summary of the dataset as follows:
reviews.groupby(['country']).price.agg([len, min, max])


countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
# To get data in the order want it in we can sort it ourselves. The sort_values() method is handy for this.
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len', ascending=False)

# To sort by index values, use the companion method sort_index(). This method has the same arguments and default order:
countries_reviewed.sort_index()

# Finally, know that you can sort by more than one column at a time:
countries_reviewed.sort_values(by=['country', 'len'])
