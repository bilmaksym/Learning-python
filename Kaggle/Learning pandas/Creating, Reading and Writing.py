import pandas as pd

# Creating a DataFrame
print(pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}))

# Not only integers can be stored inside a DataFrame also strings can be
print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland']}))

# Also we can assign values to indexes of our DataFrame
print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
                    'Sue': ['Pretty good.', 'Bland']},
                   index=['Product A', 'Product B'])
      )

# Creating a Series
print(pd.Series([1, 2, 3, 4, 5]))

# Adding new indexes and give a name to the series
print(pd.Series([30, 40, 50], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A'))

# Reading a file
#data = pd.read_csv("../")
# we can use the shape attribute to check how large the resulting DataFrame is
#print(data.shape)

# Saving a DataFrame to csv file
animals = pd.DataFrame({'Cows': [20, 19], 'Goats': [14, 21]}, index=['1 year', '2 year'])
animals.to_csv("cows_and_goats.csv")
