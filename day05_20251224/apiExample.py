# 📌 requests 삽입! ===================================================
import requests
 
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)
response.raise_for_status()  # 요청 실패 시 예외 발생
print(response.status_code)

users = response.json()

print('\n 📘 십습 1 ===========================')
print('API에서 사용자 이름(name)과 이메일(email)만 출력')

for u in users:
    print(f'name = {u['name']} | email = {u['email']} ')

print('\n 📘 십습 2 ===========================')
print('도시(city)가 "Gwenborough" 인 사용자 수를 구하기')

count = sum(1 for u in users if u['address']['city'] == 'Gwenborough' )
print(count)

print('\n 📘 십습 3 ===========================')
print('User 클래스를 사용해 이메일 도메인이 .biz 인 사용자 이름만 출력')

class User:
    def __init__( self, name, email ):
        self.name = name
        self.email = email

user_object = [ User( u['name'], u['email']) for u in users]

biz_user = [ u.name for u in user_object if u.email.endswith('.biz') ]
for name in biz_user:
    print(name)