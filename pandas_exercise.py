import pandas as pd

data = {
    'name': ['James', 'John', 'Peter'],
    'age': [10, 23, 56],
    'grade': [10, 45, 90],
}


df = pd.DataFrame(data)

# Step 2: Add "Passed" column (grade > 50)
df['Passed'] = df['grade'] > 50



# Step 3: Filter students who passed
passed_students = df[df['Passed']]




print(df)