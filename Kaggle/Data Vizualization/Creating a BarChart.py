# An example of using BarChart

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.plotting.register_matplotlib_converters()

# Firstly we need to specify path to our data
flight_data_path = "C/: ..."

# Then we need to read the data
flight_data = pd.read_csv(flight_data_path, index_col="Month")

# Now we need to specify figure size
plt.figure(figsize=(10, 6))

# Specifying title
plt.title("Average Arrival Delay for Spirit Airlines Flights, by month")

# Then let's create a bar chart according to the given title
sns.barplot(x=flight_data.index, y=flight_data['NK'])

# Add label for vertical axis
plt.ylabel("Arrival delay (in minutes)")

# Now let's create my first heatmap

plt.figure(figsize=(14.7))

plt.title("Average Arrival Delay for Each Airline, by Month")

# Creating a heatmap
sns.heatmap(data=flight_data, annot=True)

plt.xlabel("Airline")