words = [
    "python",
    "java",
    "springboot",
    "api",
    "fastapi",
    "data"
]

# 📘 실습 1 . 길이 5 이상 단어만 대문자로
print('실습 1 ===================')
upperWords = [w.upper() for w in words if len(w) >= 5]
print(upperWords)

# 📘 실습 2 . api를 포함한 문자 필터링
print('실습 2 ===================')
filterWords = [w for w in words if 'api' in w ]
print(filterWords)

class Student:
    def __init__(self, name, major, email):
        self.name = name
        self.major = major
        self.email = email

students = [
    Student("Alice", "Computer Science", "alice@school.com"),
    Student("Bob", "Data Science", "bob@school.com"),
    Student("Charlie", "Computer Science", "charlie@gmail.com"),
    Student("David", "AI", "david@school.com"),
]


# 📘 실습 3 . 학교 이메일만 추출
print('실습 3 ===================')
school_emails = [s.email for s in students if s.email.endswith('@school.com')]
print(school_emails)

# 📘 실습 4 . 전공이 Computer Science 인 학생 이름
print('실습 4 ===================')
computerMajors = [s.name for s in students if s.major == "Computer Science"]
print(computerMajors)

# 📘 실습 5 . 문자열 정규혀
print('실습 5 ===================')
raw_names = [" Alice ", "BOB", " charLie "]

normalized = [name.strip().lower() for name in raw_names]
print(normalized)