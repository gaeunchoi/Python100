import pandas as pd

df = pd.read_csv('./data/bok_statistics_CD.csv', header=None)

print(df.head(), '\n')
print(df.info())            # info() 메소드 적용 -> 데이터프레임의 자료형, 행 인덱스의 종류와 개수,
                            #                     열의 개수와 자료형, 메모리 사용량 등능의 정보 확인 가