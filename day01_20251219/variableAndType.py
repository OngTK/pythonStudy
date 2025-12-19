# 📌변수(Variable)
# 값에 이름을 붙여서 저장하는 공간

age = 25
name = "Alice"

print(age)
print(name)

# 📌파이썬 변수의 특징
# 1. 자료형을 미리 선언하지 않음
# ➡️ 파이썬은 자동으로 자료형을 판단
# ``` java
# int age = 25;
# String name = "Alice"; 
# ```

# 📌 기본 자료형(Type)
# ① 숫자
a = 10      # 정수 int
b = 3.14    # 실수 float
print(a)
print(b)

# ② 문자열 str
txt1 = "Hello"
txt2 = 'python'
print(txt1)
print(txt2)

# ③ 참/거짓 Boolean 
is_active = True
is_closed = False
print(is_active)
print(is_closed)
# ➡️ 반드시 첫글자는 대문자!!

# ④ 자료형 확인하기 Type()
print(type(a))              # <class 'int'>
print(type(b))              # <class 'float'>
print(type(txt1))           # <class 'str'>
print(type(is_active))      # <class 'bool'>

# ⑤ 변수명 규칙
# ✅ 가능
my_age = 25
user_name = "Tom"
count1 = 3

# ❌ 불가능
# 1count = 3        # 숫자로 시작 ❌
# my-age = 20       # - 사용 ❌
# class = "test"    # 예약어 ❌

