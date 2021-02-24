import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = open('./data/usa_president_message.txt', encoding='UTF-8').read()

# 워드클라우드 이미지 생성 
wordcloud = WordCloud(background_color='white', width=1920, height=1080).generate(text)

# 화면 출력 
fig = plt.figure()
plt.imshow(wordcloud, interpolation='bilinear', cmap='YlOrBr')
plt.axis('off')

# SVG 객체로 이미지 저장 
plt.savefig('./output/usa_president_message_wordcloud.svg')

