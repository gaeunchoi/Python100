import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn 제공 데이터셋 가져오기
df = sns.load_dataset('iris')
print(df.head(), '\n')
print(df.columns.values)

# 상관계수 구해서 히트맵으로 그리기
plt.figure(figsize=(10,10))
corr = df.loc[:, 'sepal_length':'petal_width'].corr()
print(corr.head(), '\n')

# 히트맵 그리기
sns.set(font_scale = 1.5)
# annot 옵션 -> 히트맵의 각 부분에 해당되는 데이터 값의 표시 여부
# square 옵션 -> 히트냅 안의 각상자모양을 정사각형으로 할 것인지
# linewidth -> 구분선의 두께, cbar -> 컬러바 따로 표시할지 여부
sns.heatmap(corr, annot=True, cmap='PuBuGn', fmt='.1f', square=True, linewidth=0.5, cbar=False)
plt.show()