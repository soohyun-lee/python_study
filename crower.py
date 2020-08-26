# import requests
# response = requests.get("https://www.naver.com")
# # print(response.status_code)
# # print(response.headers)
# print(response.text) #소켓으로 가져오는 것 / html 데이터 가져온 것

# 이미지 태그만 가져오기(beautifulsoup 많이 씀)
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com")
bs = BeautifulSoup(response.text, "html.parser") # text 데이터를 parser (파싱: 데이터에서 원하는 데이터만 추출하는것 , 그 파싱을 가능하게 하는 도구 > 파서)
for img in bs.select('img'):
    print(img)
for a in bs.select('a'):
    print(a)

#html link 가져오기(이거는 자바스크립 렌더링 할 때 주로 쓰임)
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

session = HTMLSession()
response = session.get("https://www.naver.com")
print(response.html.links)


