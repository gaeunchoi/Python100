import pandas as pd

df = pd.read_csv('./data/bok_statistics_CD.csv', header=None)

print(df.head(), '\n')          # head() 메소드를 데이터프레임 객체에 적용하면 첫 5개의 행만 선택됨
print(df.head(3), '\n')         # head(n)과 같이 매개변수에 정수값을 넣으면 해당하는 n개의 행을 리턴
print(df.tail(), '\n')          # tail() 메소드를 데이터프레임 객체에 적용하면 마지막 5개의 행만 선택됨
print(df.tail(3))               # tail(n)과 같이 매개변수에 정수값을 넣으면 해당하는 n개의 행을 추출 