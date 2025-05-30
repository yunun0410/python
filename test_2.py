import requests

# f 스트링을 이용해서 이강인이라는 값이 들어간 변수를 활용
# 문자열 +, * ->
# keyword, url 연산자 + 만을 이용해보기
# 누가 미리 만들어 놓은 기능 => 내장함수 => input()
# input 값을 입력받으면 무조건 데이터 타입은 문자형


keyword = input("검색을 원하는 키워드를 입력해주세요 : ")
# url = f"https://search.naver.com/search.naver?sm=tab_sug.top&ssc=tab.blog.all&query={keyword}"
url1 = "https://search.naver.com/search.naver?sm=tab_sug.top&ssc=tab.blog.all&query=" + keyword 

req = requests.get(url1)
print(req.text)