# 📘 아래의 숫자 리스트를 이용해 제곱 리스트 만들기 =================
numbers = [1, 2, 3, 4, 5]

# 1) lambda, map, filter
print('\n✨ lambda, map, filter ------- ')
square_list = list(
    map(lambda n : n*n ,numbers)
    )
print(square_list)

# 2) 리스트 컴프리헨션
print('\n✨ 리스트 컴프리헨션 ------- ')
square_list = [n*n for n in numbers]
print(square_list)

# 📘 아래의 단어 리스트에서 길이가 6 이상인 단어만 추출 =============
words = ["python", "java", "spring", "api", "fastapi"]

# 1) lambda, map, filter
print('\n✨ lambda, map, filter ------- ')
over_six = list(
    filter(lambda w: len(w)>=6,words)
    )
print(over_six)

# 2) 리스트 컴프리헨션
print('\n✨ 리스트 컴프리헨션 ------- ')
over_six = [ w for w in words if len(w) >= 6]
print(over_six)

# 📘 `students` 리스트에서 `@school.com` 이메일을 사용하는 학생 이름만 추출 ===
class Student : 
    def __init__(self, name, score, email):
        self.name = name
        self.score = score
        self.email = email
students = [
    Student("Alice", 90, "alice@school.com"),
    Student("Bob", 72, "bob@gmail.com"),
    Student("Charlie", 85, "charlie@school.com"),
    Student("David", 60, "david@gmail.com"),
]

# 1) lambda, map, filter
print('\n✨ lambda, map, filter ------- ')
school_email_students = list(
    map(
        lambda s : s.name,
        filter(
            lambda s : s.email.endswith("@school.com"),
            students
        )
    )
)
print(school_email_students)

# 2) 리스트 컴프리헨션
print('\n✨ 리스트 컴프리헨션 ------- ')
school_email_students = [s.name for s in students if s.email.endswith('@school.com')]
print(school_email_students)