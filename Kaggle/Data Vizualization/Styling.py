import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.plotting.register_matplotlib_converters()

spotify_filepath = "C/:..."

spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# Let's change the style
sns.set_style("dark")

# Line chart
plt.figure(figsize=(12, 8))
sns.lineplot(data=spotify_data)
