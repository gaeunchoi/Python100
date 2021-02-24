import pandas as pd

df = pd.read_csv('./data/bok_statistics_CD_2.csv', header=0, index_col=0)
print(df.head(), '\n')

df.plot(x='CD_rate', y='change', kind='scatter')