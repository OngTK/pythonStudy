# 📌 리스트 컴프리헨션 · List Comprehension ===========================
# - 리스트를 만드는 for 문을 한 줄로 압축한 문법

# 기본 형태
# 변수명 = [ 표현식 for 변수 in 반복가능한_대상 ]


# 📌 기존 for VS 리스트 컴프리헨션 ====================================
print('기존 for VS 리스트 컴프리헨션 ================')
# 🔴 기존 for 문
numbers = []
for i in range(1,6):
    numbers.append(i)
print(f'- 기존 for문 : {numbers}')

# 🟢 리스트 컴프리헨션
numbers = [ i for i in range(1,6) ]
print(f'- 리스트 컴프리헨션 : {numbers}')

# 👉 결과는 완전히 동일


# 📌 값 가공하기 (표현식) ============================================
print('\n 표현식 사용 ===========================')
squares = [i * i for i in range(1,6)]
print(squares)


# 📌 if 조건문 사용 =================================================
print('\n if ===========================')
# 짝수 리스트 만들기

# 🔴 기존 for 문
even_number = []
for i in range(1, 11):
    if i % 2 == 0 :
        even_number.append(i) 
print(f'- 기존 for : {even_number}')

# 🟢 리스트 컴프리헨션
even_number = [i for i in range(1,11) if i % 2 == 0 ]
print(f'- 리스트 컴프리헨션 : {even_number}')

# 📌 문자열 처리 ====================================================
names = ['Alice','Bob','Charlie']
upper_names = [name.upper() for name in names ] # .upper() 대문자 처리 메서드
print('\n 문자열 처리 ===================')
print(upper_names)

# 📌 class와 리스트 컴프리헨션 =======================================
class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score

# 학생 객체 리스트
students = [
    Student("Alice",90),
    Student("Bob",75),
    Student("Charlie",85)
    ]
        
# 📘 점수 리스트
scores = [student.score for student in students]
print(f'\n - 점수 리스트 : {scores}')

# 📘 80점 이상의 학생명 필터링
passed = [student.name for student in students if student.score >= 80]
print(f'\n- 합격자 리스트 : {passed}')

# 📘 if/else 합/불 출력 
# if-else 사용 시, 표현식에 조건문을 작성
results = ["합격" if s.score >= 80 else "불합격" for s in students]
print(results)