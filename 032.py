from konlpy.tag import Hannanum
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = open('./data/2018_president_message.txt', encoding='utf-8').read()

# 한글 형태소 분석
engin = Hannanum()
nouns = engin.nouns(text)
nouns = [n for n in nouns if len(n) > 1]

# 단어 숫자 세기
cnt = Counter(nouns)
tags = cnt.most_common(50)

# 워드 클라우드 이미지 생성 -> 한글폰트 패스 어케주지 ?
wordcloud = WordCloud(font_path='./data/malgun.ttf', background_color='white', width=1200, height=800).generate_from_frequencies(dict(tags))

# 화면에 출력
fig = plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

# SVG 객체로 이미지 저장
plt.savefig('./output/2018_president_message.svg')
