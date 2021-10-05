import pandas as pd
from sqlalchemy import engine

df = pd.read_sql('data.csv', con=engine, index_col='ID', columns=['COUNTRY', 'AREA'])


print(df)