import pandas as pd
from sqlalchemy import engine

df = pd.read_sql('data.db', con=engine, index_col='ID')
print(df)