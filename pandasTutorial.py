import pandas as pd

# create a dataframe (table-like structure)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'score': [85, 90, 95]
}


df = pd.DataFrame(data)
print(df)



# accessing column
print("Names:", df['Name'])


# Filter rows
print("Scores above 90:", df[df['score'] > 90])