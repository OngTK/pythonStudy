# 📌 예외처리 · Exception Handling
# 예외처리는 프로그램 실행 중 발생할 수 있는 오류 상황을 처리하는 방법
# 파이썬에서는 try, except, finally 블록을 사용하여 예외를 처리할 수 있음

# 🟢 예외 처리 발생 예:
# 파일 입출력 시 발생할 수 있는 예외 처리
# 숫자가 아닌 값을 숫자로 변환
# 0으로 나누기

# 🟢 예외 예시
# print(10 / 0)  # ZeroDivisionError 발생
# num = int("abc")  # ValueError 발생
# ⚠ 예외 발생 시 프로그램 중단

# 📌자주 발생하는 예외 ======================================
# ValueError : 잘못된 값
# ZeroDivisionError : 0으로 나누기
# FileNotFoundError : 파일을 찾을 수 없음
# TypeError : 잘못된 타입
# IndexError : 인덱스 범위 초과
# KeyError : 딕셔너리 키 없음

# 📌예외처리 기본 구조 =========================================

# try :
#     문제가 발생할 수 있는 코드
# except :
#     예외처리 코드

# 📘 예제 1: 0으로 나누기
print("예제 1: 0으로 나누기 예외 처리")
try:
    result = 10 / 0
    print("결과:", result)
except:
    print("예외 발생: 0으로 나눌 수 없습니다.")
print("프로그램 계속 실행됨\n")


# 📌 특정 예외 처리=========================================

# try :
#     문제가 발생할 수 있는 코드
# except 예외타입1 :
#     예외처리 코드1
print("\n예제 2: 특정 예외 처리 - ZeroDivisionError")
try:
    result = 10 / 0
    print("결과:", result)
except ZeroDivisionError:
    print("예외 발생: 0으로 나눌 수 없습니다.")
# ⚠ 무조건 except 보다는 특정 예외 타입을 지정하는 것이 좋음✨✨

# 📌 여러 예외 처리 ========================================
print("\n예제 3: 여러 예외 처리 - ZeroDivisionError, ValueError")
try :
    num = int(input("숫자를 입력하세요: "))
    result = 10 / num
    print("결과:", result)
except (ZeroDivisionError, ValueError):
    print("예외 발생: 0으로 나누거나 숫자로 변환할 수 없습니다.")

# 📌 예외 정보 얻기 ========================================
print("\n예제 4: 예외 정보 얻기")
try:
    result = 10 / 0
    print("결과:", result)
except ZeroDivisionError as e:
    print("예외 발생:", e)

# 📌 else / finally =======================================
# else : 예외가 발생하지 않을 때 실행되는 코드 블록
print("\n예제 5: else 사용")
try:
    x = int(input("숫자: "))
except ValueError:
    print("숫자가 아닙니다.")
else:
    print("입력 성공:", x)

# finally : 예외 발생 여부와 상관없이 항상 실행되는 코드 블록
print("\n예제 5: finally 사용")
try:
    f = open("test.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    print("프로그램 종료")

# 📌 사용자 정의 예외 =======================================
# 사용자 정의 예외는 프로그래머가 직접 예외 클래스를 정의하여 사용하는 방식
print("\n예제 6: 사용자 정의 예외")
class NegativeNumberError(Exception):
    pass
def check_positive(num):
    if num < 0:
        raise NegativeNumberError("음수는 허용되지 않습니다.")
    
try:
    check_positive(-5)
except NegativeNumberError as e:
    print("예외 발생:", e)

# 📌 예외 전파 ===========================================
# 예외는 함수 호출 스택을 따라 전파되며, 예외가 처리되지 않으면 프로그램이 종료됨
print("\n예제 7: 예외 전파")
def func_a():
    func_b()    
def func_b():
    func_c()
def func_c():
    raise ValueError("예외가 발생했습니다.")

try:
    func_a()
except ValueError as e:
    print("예외 발생:", e)