import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

# BeautifulSoup 함수는 매개변수로 전달반은 HTML 소스코드를 해석하여 객체를 생성해
# HTML을 파밍(해석)하는 적절한 구문해석기(parser)를 함께 입력해야해 -> 여기서 html.parser 사용했오
soup = BeautifulSoup(html_src, 'html.parser')
print(type(soup))
print("\n")

print(soup.head)
print("\n")
print(soup.body)
print("\n")

print('title 태그 요소: ', soup.title)
print('title 태그 이름: ', soup.title.name)
print('title 태그 문자열: ', soup.title.string)