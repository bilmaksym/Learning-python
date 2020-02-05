import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.plotting.register_matplotlib_converters()

# Define path to the data
iris_path = "C/: ..."

# Load the data
iris_data = pd.read_csv(iris_path, index_col="Id")

# Print the first five rows of the data
iris_data.head()

# Creating a histogram
sns.distplot(a=iris_data['Petal Length (cm)'], kde=False)

# Creating a KDE plot
sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)

# Creating a 2D KDE plot
sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")

