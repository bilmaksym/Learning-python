import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.plotting.register_matplotlib_converters()


# Firstly we need to establish path for our data
data_path = "C/:..."

# Then we need to read the file (for example csv) using pandas
test_data = pd.read_csv(data_path, index_col="Date", parse_dates=True)

# Print the first 5 rows of the data
print(test_data.head())

# Now let's set the width and height of the figure
plt.figure(figsize=(14, 6))

# Add title
plt.title("Your title")

# Plot the data
sns.lineplot(data=test_data)

# Show our plot
plt.show()

# Another example. Now we are only want to show first 2 columns
sns.lineplot(data=test_data['Shape of You'], label="Shape of You")
sns.lineplot(data=test_data['Despacito'], label="Despacito")

# Add label for horizontal axis
plt.xlabel("Date")
