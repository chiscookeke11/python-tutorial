import pandas as pd

# Creating DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', "Chinedu"],
        'Age': [25, 30, 35, 45],
        'City': ['New York', 'Los Angeles', 'Chicago', 'New York']}

df = pd.DataFrame(data)
print(df)


# Read data from a CSV file
# read_df = pd.read_csv('data.csv')

# Manipulating DataFrames:

# Selecting Columns: You can select a specific column like this:
df['Age']  # Selects the Age column


# Filtering Rows: You can filter rows based on a condition:
df[df['Age'] > 30]  # Returns rows where Age > 30

# Filtering data based on multiple conditions
df_multifiltered = df["Name"][(df['Age'] >= 25) & (df['City'] == "New York")]
print(df_multifiltered)


# Adding Columns:
df['Country'] = ['USA', 'USA', 'USA', 'USA']  # Adds a new column


# Removing Columns
df.drop('Country', axis=1, inplace=True)  # Drops the 'Country' column





# sorting data
# sorting by columns
df_sorted = df.sort_values(by='Age', ascending=False)

# sorting by multiple columns
df_sorted = df.sort_values(by=['Age', 'City'], ascending=[True, False])
print(df_sorted)



# Aggregating data
# Groupby: pandas groupby method is essential for aggregating data based on one or more columns. For example:

grouped = df.groupby('City').agg({'Age': 'mean', 'Name': 'count'})
print(grouped)




# Summary Statistics: pandas provide several built-in functions to calculate summary statistics:
print(df['Age'].mean())  # Mean of 'Age' column
print(df['Age'].sum())   # Sum of 'Age' column
print(df['Age'].max())   # Maximum of 'Age' column