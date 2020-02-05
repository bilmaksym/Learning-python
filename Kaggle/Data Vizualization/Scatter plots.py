# Here is example of using scatter plots

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.plotting.register_matplotlib_converters()


# Path to the file to read
insurance_filepath = "C/: ..."

# Read the file into a variable insurance_data
insurance_data = pd.read_csv(insurance_filepath)

# Print the first five rows
insurance_data.head()

# Creating a scatter plot
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# !!! Let's create plot with regression line to double-check the correlation between body mass index (bmi) and charges !!!
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# Scatter plot with colored points to see how not two but three variables correlates among each other
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])

# Scatter plot with two regression lines and colored points
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)

# Categorical scatter plot
sns.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])

