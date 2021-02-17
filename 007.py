import requests, re
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')

# 같은 조건을 만족하는 모든 태그를 찾을 때 find_all() 메소드 사용
links = soup.find_all("a")                  # 모든 <a> 태그를 찾고 변수 links에 저장해
print("하이퍼링크 개수: ", len(links))
print("\n")
print("첫 3개의 원소: ", links[:3])
print("\n")

# <a> 태그의 href 속성이 포함하는 문자열을 따로 지정하면, 해당 문자열이 포함된 <a> 태그만을 찾아
# '/wiki/' 문자열이 링크에 포함되어 있는 <a> 태그 3개를 wiki_links에 저장해
wiki_links = soup.find_all(name = "a", href = re.compile("/wiki/"), limit = 3)      # 여기선 출력 길이를 제한하기위해 limit 매개변수는 3으로 설정
print("/wiki/ 문자열이 포함된 하이퍼링크: ", wiki_links)
print("\n")

# class 속성값이 "external text"인 <a> 태그를 모두 찾아서 리스트 형태로 리턴
# 여기도 limit 매개변수를 3으로 설정하여 3개까지 추출
external_links = soup.find_all(name = "a", attrs = {"class" : "external text"}, limit = 3)
print("class 속성으로 추출한 하이퍼링크: ", external_links)