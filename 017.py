import pandas as pd
import xlrd

csv_file = './data/bok_statistics_CD.csv'

#read_csv() 함수로 데이터프레임 변환
df1 = pd.read_csv(csv_file)
print(df1)
print('\n')

# header=None 옵션을 준 경우 -> csv 파일의 모든 행이 데이터프레임의 행으로 변환, 열의 이름은 0~2로 자동 지정
df2 = pd.read_csv(csv_file, header=None)
print(df2)
print('\n')

# index_col=0 옵션을 준 경우 -> csv 파일의 0열(첫 번째 열)이 행 인덱스로 변환
df3 = pd.read_csv(csv_file, index_col=0)
print(df3)
print('\n')

# index_col=0, header=None 옵션 모두 준 경우
df4 = pd.read_csv(csv_file, index_col=0, header=None)
print(df4)
print('\n')

excel_file = './data/report_Key100Stat.xls'

df5 = pd.read_excel(excel_file)
print(df5)