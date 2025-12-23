# 📌 객체지향 프로그래밍 · Object Oriented Programing

# 🔴 함수 방식
def deposit(balance, amount):
    return balance + amount
# 데이터와 행동이 분리됨
# 코드가 커질수록 관리가 어려음

# 🟢 객체지향 방식
# account.deposit(500)
# 👉 데이터와 행동을 하나로 묶음

# 📌 클래스 · Class ===================================================
# 객체를 만들기 위한 설계도
# class 키워드 사용
# 클래스명은 대문자로 시작

class Person :
    pass

# 📌 객체 · Object ====================================================
# 클래스를 기반으로 생성된 실제 인스턴스
p1 = Person()
p2 = Person()
# p1과 p2는 서로 다른 객체

# 📌 생성자 `__init__` ✨✨✨ ========================================
# 객체가 생성될 때 자동으로 실행되는 함수
# `self`
# - 객체 자기 자신
# 모든 인스턴스 메소드의 첫번째 인자

class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("배두훈", 40)
print('객체 생성 ===========')
print(p.name)
print(p.age)

# 📌 메서드 · Methon ===================================================
class Person : 
    def __init__(self, name):
        self.name = name
    
    def say_hello(self) :
        print(f"Hello, I`m {self.name}")

print('\n메소드 ============')
p = Person("강형호")
p.say_hello()

# 📌 속성 · Attribute VS 메소드 · Method

# |  구분  |  의미  |     예      |
# |-------|-------|-------------|
# |  속성  | 데이터 |  name, age  |
# | 메서드 |  행동  | say_hello() |

# 📘 실전 예제 · 계좌 클래스 ==============================================

class Account:
    # 생성자 
    def __init__(self, owner, balance):
        self.owner = owner          # 계좌주
        self.balance = balance      # 잔액
        print(f'\n계좌생성_계좌주 : {self.owner} | 계좌잔액 : {self.balance} 원')
    
    # 메서드 1 : 입금
    def deposit(self, amount):
        print(f'\n입금 실행 -----')
        print(f'입금 전 잔액 : {self.balance}')
        self.balance += amount
        print(f'입금 후 진액 : {self.balance}')


    # 메서드 2 : 출금
    def withdraw(self, amount):
        print(f'\n출금 실행 -----')
        if amount > self.balance :
            print("잔액부족")
        else:
            print(f'출금 전 금액 : {self.balance}')
            self.balance -= amount
            print(f'출금 전 금액 : {self.balance}')

# class end

print('계좌 예제 =======================')
acc = Account("조민규", 10000)
acc.deposit(50000)
acc.withdraw(20000)