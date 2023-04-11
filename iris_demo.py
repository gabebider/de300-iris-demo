import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV file
data = pd.read_csv('iris.csv')

data = data.iloc[:, :-1]

fig, ax = plt.subplots()

ax.boxplot(data.values)

ax.set_xticklabels(data.columns)

ax.set_title("Boxplots of Iris Data")

# plt.show()
plt.savefig('iris.png')

# # Loop through each column in the data
# for i, column in enumerate(data.columns):
#     # Create a box plot for the column
#     if i < 4:
#         plt.boxplot(data[column])
#         plt.title(column)
#         plt.show()