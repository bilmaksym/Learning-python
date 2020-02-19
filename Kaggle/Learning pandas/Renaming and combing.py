import pandas as pd
pd.set_option('max_rows', 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# Let's explore rename() function which is using to rename columns and indexes
reviews.rename(columns={'points': 'score'})

# Let's see another example for index
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})

# Both the row index and the column index can have their own name attribute. The complimentary rename_axis() method may be used to change these names. For example:
reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')

# Lets explore concat() and join() function to combine data from different DataFrames and Series
canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")

pd.concat([canadian_youtube, british_youtube])

# join() let us combine different DataFrames objects which have an index in common. Example:
left = canadian_youtube.set_index(['title', 'trending_data'])
right = british_youtube.set_index(['title', 'trending_data'])

left.join(right, lsuffix='_CAN', rsuffix='_UK')

# The lsuffix and rsuffix parameters are necessary here because the data has the same column names in both
# British and Canadian datasets. If this wasn't true (because, say, we'd renamed them beforehand) we wouldn't need them.
