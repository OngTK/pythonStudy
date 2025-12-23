# 📘 실습 1 ===============================================
print('\n - 실습 1')
# 1~20 중에서
# 홀수만 리스트로 만드세요.

list1 = [ i for i in range(1,21) if i % 2 == 1 ]
print(list1)

# 📘 실습 2  ===============================================
print('\n - 실습 2')
# 문자열 리스트에서
# 길이가 5 이상인 단어만 대문자로 변환하세요.
strings = [
    "cat",
    "python",
    "database",
    "api",
    "spring",
    "react",
    "cloud",
    "lambda"
]

list2 = [s.upper() for s in strings if len(s) >= 5]
print(list2)

# 📘 실습 3 (객체 연계)  ====================================
print('\n - 실습 3')
# Student 객체 리스트에서
# 점수가 80 이상인 학생 이름만 리스트로 추출하세요.

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [
    Student("alice", 85),
    Student("bob", 92),
    Student("charlie", 78),
    Student("david", 88),
    Student("emma", 95),
    Student("frank", 67),
    Student("grace", 90),
    Student("henry", 73),
    Student("irene", 81),
    Student("jack", 89)
]

over80List = [s.name for s in students if s.score >= 80]
print(over80List)