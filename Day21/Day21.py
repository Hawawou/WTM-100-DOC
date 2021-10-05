import pandas as pd

df = pd.read_csv('data.csv', index_col=0, na_values='(missing)')
df.types 

