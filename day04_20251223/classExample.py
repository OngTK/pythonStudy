### 📘 실습 1

# `Student` 클래스
# - 속성: 이름(name), 점수(score)
# - 메서드: 점수 출력(show_score)

class Student:
    # 생성자
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def show_score(self):
        print(f'점수 : {self.score}')

print(f'실습 1 ==================')
stu1 = Student("고우림",99)
stu1.show_score()

# ============================================

### 📘 실습 2

# `Calculator` 클래스
# - 메서드: add(a, b), sub(a, b)

class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        print(f'더하기 : {a + b}')

    def sub(self, a, b ):
        print(f'빼기 : {a - b }')

print(f'실습 2 ==================')
cal = Calculator()
cal.add(3,9)
cal.sub(20,13)