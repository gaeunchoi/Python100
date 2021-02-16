import requests

urls = ["https://www.naver.com/", "https://www.python.org/"]
filename = "robots.txt"

for url in urls :
    file_path = url + filename
    print(file_path)

    resp = requests.get(file_path)
    print(resp.text)        # 웹서버 응답 객체 text 속성은 HTML 소스를 저장하고 있어서 print()로 출력하면 각 사이트의 로봇 배제 표준의 내용 볼수이써
    print("\n")


# naver의 로봇 배제 표준-> 모든 로봇에 대하여 모든 디렉토리 접근 금지(Disallow: /)
#                     -> 다만 "Allow: /$"와 같이 "/"로 끝나는 디렉토리에 한하여 허용. 즉 루트 디렉토리에 한하여 로봇의 접근 허용
#                     -> "$"는 마지막 부분이라는 뜻이랭

# python 공식 홈페이지 로봇 배제 표준 -> 일부 로봇(HTTrack, puf, MSIECrawler)의 접근을 금지하고있지
#                                 -> 대부분의 로봇에 대해서는 일부 티렉토리(/~guido/orlijn/, /webstats/)를 제외하고 접근 허락함