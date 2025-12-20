# 📌반복문 ( for / while )

# 📌for 문 ===============================================
# for 변수 in 반복가능한객체(리스트, 튜플, 문자열):
#     반복할 코드   

# 🔹 range(끝값)
print("range(끝값) 예제:")
for i in range(5):  # 0 ~ 4
    print(i)
# 출력: 0 1 2 3 4

# 🔹 range(시작값, 끝값, 증가값)
print("range(시작값, 끝값, 증가값) 예제:")
for i in range(1, 10, 2):  # 1 ~ 9, 2씩 증가
    print(i)
# 출력: 1 3 5 7 9

# 🔹 리스트 순회
print("리스트 순회 예제:")
for i in [10, 20, 30]:
    print(i)
# 출력: 10 20 30

# 🔹 문자열 순회
print("문자열 순회 예제:")
for char in "Hello":
    print(char)
# 출력: H e l l o

# 📌while 문 =============================================
# while 조건식:
#     반복할 코드   
#     조건식이 참인 동안 반복 실행

# 🔹예제
print("while 문 예제:")
count = 0
while count < 5:
    print(count)
    count += 1  # count = count + 1
# 출력: 0 1 2 3 4

# ❌ 무한 루프 주의!
# while True:
#     print("무한 루프")
# 출력: 무한 루프가 계속 출력됨
# 무한 루프를 멈추려면 Ctrl + C (터미널) 또는 중지 버튼(IDE)을 사용

# 📌break 와 continue (반복문 제어 키워드) ====================================
# - break: 반복문을 즉시 종료
# - continue: 현재 반복을 건너뛰고 다음 반복으로 이동

# 🔹 break 예제
print("break 예제:")
for i in range(10):
    if i == 5:
        break  # i가 5일 때 반복문 종료
    print(i)
# 출력: 0 1 2 3 4

# 🔹 continue 예제
print("continue 예제:")
for i in range(10):
    if i == 5:
        continue  # i가 5일 때 현재 반복 건너뛰기
    print(i)
# 출력: 0 1 2 3 4 6 7 8 9

# 🔹 while 문에서 break와 continue 예제
print("while 문에서 break와 continue 예제:")
count = 0
while count < 10:
    count += 1
    if count == 5:
        continue  # count가 5일 때 현재 반복 건너뛰기
    if count == 8:
        break     # count가 8일 때 반복문 종료
    print(count)
# 출력: 1 2 3 4 6 7

# 🟢 실습 1
# 1부터 100까지의 합을 구하세요.
sum = 0
for i in range(1,101):
    sum += i
print(f"1부터 100까지의 합: {sum}")

# 🟢 실습 2
# 사용자로부터 숫자를 받아 구구단을 출력
num = int(input("구구단을 출력할 숫자를 입력하세요: "))
print(f"{num}단 출력:")
for i in range(1, 10):
    print(f"{num} x {i} = {num * i}")

# 🟢 실습 3
# 1부터 50까지의 숫자 중 짝수의 합을 구하세요.
even_sum = 0
for i in range(1, 51):
    if i % 2 == 0:
        even_sum += i   
print(f"1부터 50까지의 짝수의 합: {even_sum}")
