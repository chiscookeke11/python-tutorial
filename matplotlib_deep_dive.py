import matplotlib.pyplot as plt
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', "Chinedu"],
        'Age': [25, 30, 35, 45],
        'City': ['New York', 'Los Angeles', 'Chicago', 'New York']}

df = pd.DataFrame(data)


# Plotting a scatter plot of Age vs. City
df.plot(kind='scatter', x='City', y='Age')
plt.title('City vs Age')
plt.show()








# Best Practices for Working with Data and Basic Data Analysis:

# Data Cleaning: Before analysis, always ensure the data is clean. This includes handling missing values (df.fillna()), removing duplicates (df.drop_duplicates()), and dealing with outliers.

# Efficient Data Access: pandas provides several ways to read large datasets efficiently. For example, use chunksize to read large CSV files in chunks.

# Handling Data Types: Ensure the data types of your columns are correct (e.g., using df['Age'] = df['Age'].astype(int)).

# Documentation: When working on analysis, make sure to document your code and the reasoning behind each transformation or computation.