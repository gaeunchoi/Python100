import pandas as pd

df = pd.read_csv('./data/bok_statistics_CD.csv', header=None)

print(df.head(), '\n')
print(df.describe())        # describe() 메소드 적용 -> 각 열의 데이터개수(count), 평균값(mean), 표준편차(std), 최소값(min)~최대값(max) 및 사분위값 확인 가능 