import pandas as pd

df = pd.read_csv('./data/bok_statistics_CD.csv', header=None)
print(df.head(), '\n')

df.columns = ['year', 'CD_rate', 'change']      # 열 이름
df.set_index('year', inplace=True)              # year 열을 행 인덱스로 설정
print(df.head())
df.to_csv('./data/bok_statistics_CD_2.csv')
print('\n')

df.plot()

df['CD_rate'].plot()
df['change'].plot()