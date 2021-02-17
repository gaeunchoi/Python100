import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')

links = soup.select('a')
print(len(links))
print("\n")

print(links[:3])
print("\n")

external_links = soup.select('a[class = "external text"]')
print(external_links[:3])
print("\n")

# CSS의 id 선택자 활용 -> CSS에서 id는 고유한 값 -> select() 메소드에 id 선택자를 사용하면 오직 한 개의 태그만 찾아
id_selector = soup.select('#siteNotice')            # id 속성값이 "siteNotice" 인 태그를 가리킴
print(id_selector)
print("\n")

# 특정 태그 안에서만 id 선택자를 찾는 방법도 이써
id_selector2 = soup.select('div#siteNotice')        # div 태그 중에서 id 속성값이 "siteNotice" 인 div 태그를 뜻해
print(id_selector2)
print("\n")

id_selector3 = soup.select('p#siteNotice')          # p 태그중에서 id 속성값이 "siteNotice" 인 p 태그
print(id_selector3)
print("\n")

# CSS의 클래스 선택자 활용 -> CSS에서 서로 다른 요소에 동일한 스타일을 지정할 때 클래스 선택자 사용 -> 같은 클래스를 갖는 여러 태그 동시에 찾을 수 있어
# 클래스 선택자는 ".class속성값"으로 표현해
class_selector = soup.select('.mw-headline')        # class 속성값이 mw-headline에 해당하는 모든  태그를 뜻해
print(class_selector)
print("\n")

# 클래스 선택자의 경우에도 특정 태그에 한정하여 적용할 수 있지롱
class_selector2 = soup.select('span.mw-headline')   # <span> 태그 중에서 class 속성 값이 mw-headline에 해당하는 태그를 뜻해
print(class_selector2)