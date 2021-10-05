import pandas as pd 

dtypes = {'POP': 'float32', 'AREA': 'float32', 'GDP': 'float32'}
df = pd.read_csv('data.csv', index_col=0, dtype=dtypes, parse_dates=['IND_DAY'])
print(df.types)

#values separator, data separated with a ;
s = df.to_csv(sep=';', header=False)
print(s)