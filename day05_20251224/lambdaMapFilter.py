# 📌 사용 상황에 따른 비교
'''
| 상황              | 추천            |
|------------------|----------------|
| 단순 필터/변환     | 리스트 컴프리헨션 |
| 함수형 스타일      | map / filter   |
| 복잡한 로직        | 일반 함수       |
| API 응답 파이프라인 | map + filter   |

'''

# 📌lambda ================================================
# - 이름 없는 한 줄 짜리 함수
# - 특징
#       - 한 줄
#       - return 키워드 없음
#       - 즉석 함수

# 🟢 일반 함수
def add(a,b):
    return a+b

# 🟢 lambda함수
print('✨ add 람다 함수 ------ ')
add = lambda a,b : a+b
print( add(3,5) )

# 제곱을 반환하는 람다함수
square = lambda a : a*a
print('\n✨ square 람다 함수 ------ ')
print(square(4))

# 📌Map =====================================
# 모든 요소를 변환

# ✔ 기본 구조
#  map(함수, 반복가능한 데이터)

words = ["python", "java", "fastapi", "data"]

# 📘 모든 단어를 대문자로 변환
print('\n✨ Map 대문자 변환 ------ ')
result = list(map(lambda w: w.upper(), words))
print(result)

# VS 리스트컴프리헨션
result = [w.upper() for w in words]
print('\n✨ 리스트 컴프리헨션 ------ ')
print(result) 

# 📌 Filter ==================================
# 조건에 맞는 요소만 선별

# ✔ 기본구조
# filter(조건함수, 반복가능한 데이터)

# 📘 길이 5 이상의 단어
print('\n✨ 길이 5 이상의 단어 ------- ')
result = list(filter(lambda w: len(w) >= 5 , words))
print(result)

# VS 리스트컴프리헨션
result = [w for w in words if len(w) >= 5]
print('\n✨ 리스트 컴프리헨션 ------ ')
print(result) 

# 📌Map + Filter 조합 ==========================
# 📘 길이 5 이상을 대문자로 변환한 리스트
print('\n✨ Map+Filter 길이 5 이상의 단어를 대문자화 -----')
result = list(
    map(
        lambda w : w.upper(),
        filter(lambda w : len(w) >= 5, words)
    )
)
print(result)

print('\n✨ 리스트 컴프리헨션 ------- ')
result = [ w.upper() for w in words if len(w) >= 5]
print(result)


# 📌 객체지향과 람다식 ============================

# ① 📘 점수 80점 이상의 이름 추출 -----------------
# 1) 클래스 선언
class Student : 
    def __init__(self, name, score, email):
        self.name = name
        self.score = score
        self.email = email
# 2) 샘플데이터
students = [
    Student("Alice", 90, "alice@school.com"),
    Student("Bob", 72, "bob@gmail.com"),
    Student("Charlie", 85, "charlie@school.com"),
    Student("David", 60, "david@gmail.com"),
]

# 1) lambda, map, filter
print('\n✨ lambda, map, filter ------- ')
passed_name = list(
    map(
        lambda s : s.name,
        filter(lambda s : s.score >= 80 ,students)
    )
)
print(passed_name)

# 2) 리스트 컴프리헨션
print('\n✨ 리스트 컴프리헨션 ------- ')
passed_name = [s.name for s in students if s.score>=80]
print(passed_name)

# ② 📘 이메일 리스트 중 test.com 도메인만 추출
emails = [
    "admin@test.com",
    "user@gmail.com",
    "manager@test.com",
    "guest@yahoo.com"
]

# 1) lambda, map, filter
print('\n✨ lambda, map, filter ------- ')
test_email = list(
    filter(lambda e : e.endswith("test.com"),emails)
    )
print(test_email)

# 2) 리스트 컴프리헨션
print('\n✨ 리스트 컴프리헨션 ------- ')
test_email = [e for e in emails if e.endswith("test.com")]
print(test_email)