import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')

# select는() 메소드가 리턴하는 객체를 변수 subway_image에 저장 -> select() 메소드 파이썬 리스트를 리턴해
# CSS 선택자를 이용하여 같은 레벨에 있는 다른  태그까지 한꺼번에 선택할 수 있어
subway_image = soup.select('#mw-content-text > div.mw-parser-output > table:nth-child(3) > tbody > tr:nth-child(2) > td > a > img')
print(subway_image)             # subway_image 변수는 원소 1개(<img> 태그)를 갖는다
print("\n")
print(subway_image[0])          # HTML 요소(<img> 태그) 부분만을 따로 추출하려면 파이썬 리시트위 원소 인덱싱을 사용해
print("\n")

# 원본 CSS 선택자에서 태그  이름만 남겨서 select() 메소드에 입력해
# ">" 표시는 자식 선택자를 나타냄. tr 태그 안에 바로 이어지는 td 하위 태그를 가리켜
# 반면, tr 태그 안에 들어있는 모든 td 하위 태그를 선택할 때는 "tr td"와 같이 후손 선택자를 사용해
subway_image2 = soup.select('tr > td > a > img')
print(subway_image2[1])