import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')

# find() 메소드에 HTML 태그이름('img')을 전달하면 해당하는 태그 요소를 찾을 수 있어
first_img = soup.find(name='img')
print(first_img)
print("\n")

# find() 메소드의 attrs 매개변수에 {'속성 이름' : '속성값'}의 딕셔너리 구조의 태그가 갖는 고유의 속성값을 지정함
# 지정한 속성값을 갖는  ㅐ그 중에서 가장 처음 나오는 태그를 찾아
# attrs 매개변수에 alt 속성 이외의 다른 속성도 넣을 수 있지롱
target_img = soup.find(name = 'img', attrs = {'alt':'Seoul-Metro-2004-20070722.jpg'})
print(target_img)