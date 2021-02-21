from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 통계지표 검색어를 입력하여, CSV 파일로 저장
def download_bok_statistice_by_keyword():
    item_found = 0                      # 아래 내려가서 키워드를 찾으면 1(True)로 바꿀거야
    while not item_found:               # item_found값이 False이면 계속 while문을 실행해
        keyword = ""                    # 검색어 초기화
        while len(keyword) == 0:
            keyword = str(input("검색할 항목을 입력하세요: "))

        # 웹드라이버 실행
        driver = webdriver.Chrome("./venv/lib/python3.7/site-packages/selenium/chromedriver")
        driver.implicitly_wait(3)
        driver.get("http://ecos.bok.or.kr/jsp/vis/keystat/#/key")
        time.sleep(5)

        items1 = driver.find_elements_by_css_selector('a[class="ng-binding"]')
        items2 = driver.find_elements_by_css_selector('a[class="a-c1-list ng-binding"]')
        items3 = driver.find_elements_by_css_selector('a[class="a-c4-list ng-binding"]')
        driver.implicitly_wait(3)

        # items1의 첫번째 원소는 웹 페이지 왼쪽 위에 있는 버튼 -> items1[1:]과 같이 제외시킴
        items = items1[1:] + items2 + items3

        # enumerate() -> 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
        for idx, item in enumerate(items):              # for문을 이용해서 items 리스트에 들어있는 HTML 요소를 하나씩 꺼내어 처리
            if keyword in item.text:                    # item 객체의 text 값에 keyword 문자열이 포함되어있으면 True니까 다음 문장으로 고고
                print("검색어 '%s'에 매칭되는 '%s' 통계지표를 검색중 " % (keyword, item.text))
                item.click()                            # click() 메소드로 item 요소를 마우스로 클릭하는 동작 수행해
                item_found = 1                          # item_found값 1(True)로 변경
                time.sleep(5)
                break                                   # break로 while문 탈출 후 프로그램 처리
            elif idx == (len(items) - 1):               # items에 들어있는 마지막 item까지 keyword값이 포함되는 item을 찾지 못한 경우
                print("검색어 '%s'에 대한 통계지표가 존재하지 않습니다 " % keyword)
                driver.close()                          # 크롬 웹드라이버 종료시킬거양
                continue                                # 그리고 다시 10번 라인의 while 반복문 처리
            else:
                pass                                    # 나머지 경우에는 아무런 작업도 수행 안해용

    # 검색결과 로딩 HTML 웹 페이지 파싱 -> 통계지표 테이블(표) 양식 정리
    html_src = driver.page_source                       # 선택된 드라이버에는 통게지표 상세정보 페이지 로딩되어있음 -> HTML 소스코드 가져오기
    soup = BeautifulSoup(html_src, 'html.parser')       # BeautifulSoup으로 파싱한 결과 soup에 저장하구
    driver.close()                                      # 크롬 웹드라이버 종료해

    table_items = soup.find_all('td', {'class':'ng-binding'})               # td 태그 중에서 class 속성값이 ng-binding인 모든 태그 찾기
    date = [t.text for i, t in enumerate(table_items) if i % 3 == 0]        # 시점
    value = [t.text for i, t in enumerate(table_items) if i % 3 == 1]       # 지표
    change = [t.text for i, t in enumerate(table_items) if i % 3 == 2]      # 전기대비증감

    # CSV 파일로 저장
    result_file = open('./data/bok_statistics_%s.csv' % keyword, 'w')       # 추출한 값 CSV 파일로 저장

    for i in range(len(date)):
        result_file.write("%s, %s, %s" % (date[i], value[i], change[i]))
        result_file.write('\n')

        result_file.close()
        print("키워드 '%s'에 대한 통계 지표를 저장하였습니다." % keyword)

        return date, value, change                      # 함수 리턴값을 (날짜, 통계값, 변화율) 형식의 튜플로 정의 -> 튜플의 원소는 리스트 자료형이야

# 함수 실행 -> 'CD수익률' 통게지표를 별도로 검색 -> CSV 파일로 저장
result = download_bok_statistice_by_keyword()
print(result)