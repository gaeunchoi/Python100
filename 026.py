import pandas as pd

df = pd.read_csv('./data/bok_statistics_CD_2.csv', header=None, index_col=0)
print(df.head(), '\n')

df.plot(kind='bar')

df['CD_rate'].plot(kind='bar')
df['change'].plot(kine='bar')