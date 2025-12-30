import pandas as pd


df = pd.read_csv('email.csv', sep=';')
print(df.columns)
print(df['Login email'])

