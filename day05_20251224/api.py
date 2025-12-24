# 📌 API 실행에 앞서서 가상환경 세팅 필요!!!
# - 가상 환경 생성
#   Windows: `python -m venv venv`
# - 가상 환경 활성화
#   Windows: `venv\Scripts\activate`
# - 활성화 완료되면 터미널의 프로젝트 경로 앞에 [ (venv) ]가 표시됨
# - 가상 환경 비활성화
#   `deactivate` 명령어 입력

# 📌 request 설치 (at 가상환경) =============================
# 최초 1회
# pip install requests

# 📌API 호출 = GET ========================================
import requests
url = 'https://jsonplaceholder.typicode.com/users'

print(' ✨ 샘플 URL GET! ===========================')
response = requests.get(url)
print('\n ✨ response status_code ')
print(response.status_code) 
# 출력: 200

# 📌 JSON 응답 처리 ✨✨✨ ================================
users = response.json()
# json = api 응답은 리스트 + 딕셔너리 구조
print('\n ✨ users의 타입 =========================')
print(type(users))

print('\n ✨ users 전문 ===========================')
# print(users)

# 📌 데이터 가공 ============================================

# 📘 모든 사용자의 이름 추출
print('\n ✨ 1. 모든 사용자의 이름 추출 ==============')

print('\n ✨ 리스트 컴프리헨션 ----------------------')
names = [u["name"] for u in users]
print(names)

print('\n ✨ map/filter --------------------------')
names = list(map(lambda u : u["name"], users))
print(names)

# 📘 이메일만 추출
print('\n ✨ 2. 이메일만 추출 =======================')

print('\n ✨ 리스트 컴프리헨션 ----------------------')
emails = [ u['email'] for u in users ]
print(emails)

print('\n ✨ map/filter --------------------------')
emails = list(map(lambda u : u['email'],users))
print(emails)


# 📘 특정 도시(Gwenborough)의 사용자 이름 필터링 
print('\n ✨ 3. 특정 도시 사용자만 필터링 =============')

print('\n ✨ 리스트 컴프리헨션 ----------------------')
city_user = [ u['name'] for u in users if u['address']['city'] == "Gwenborough"]
print(city_user)

print('\n ✨ map/filter --------------------------')
city_user = list(
    map(
        lambda u : u['name'],
        filter(lambda u : u['address']['city'] == "Gwenborough", users)
        )
    )
print(city_user)

# 📌객체지향으로 확장 =======================================
# 🟢 User 클래스 정의
class User:
    def __init__(self, name, email, city):
        self.name = name
        self.email = email
        self.city = city

# 🟢 API → 객체 변환 (리스트 컴프리헨션)
print('\n ✨ User 객체 변환 =============')
user_object = [
    User(
        u['name'],
        u['email'],
        u['address']['city']
    ) for u in users
]
print(user_object)
# 출력
# [<__main__.User object at 0x0000022112D95BE0>, 
# <__main__.User object at 0x0000022112E50910>,
# ...]

# 🟢 객체 → 리스트 처리
city_users = [u.name for u in user_object if u.city == "Gwenborough"]
print(city_users)

# 📌 API 요청시 자주 쓰는 옵션
# 🟢 파라미터
#  requests.get(url, params={"id":1})
# 🟢 헤더
# requests.get(url, headers={"Accept":"application/json"})