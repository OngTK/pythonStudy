# 📌 messages
#       1회성 알림(플래시 메시지) 를 저장/표시하는 기능
#       저장 위치는 세션/쿠키 기반이며, “한 번 출력되면 사라지는” 용도
from django.contrib import messages
# 📌 login(request, user) 
#       : 로그인 처리(세션에 사용자 정보 기록)
# 📌 logout(request) 
#       : 로그아웃 처리(세션에서 사용자 제거)
# 📌 authenticate() 
#       : 아이디/비번 검증해서 user를 찾아주는 함수(일반적으로 로그인 구현에서 많이 사용)
from django.contrib.auth import authenticate, login, logout
# 📌 AuthenticationForm
#       Django가 기본 제공하는 로그인 폼
#       username/password 필드 + 검증 로직이 포함
# form.is_valid()가 True면, 내부적으로 authenticate()가 성공한 상태
from django.contrib.auth.forms import AuthenticationForm
# 📌 render() 
#       : 템플릿 렌더링 + context 전달
# 📌 redirect() 
#       : URL로 리다이렉트(POST 성공 후 페이지 이동에 자주 사용)
from django.shortcuts import render, redirect
# 📌 직접만든 회원가입 form (대부분 UserCreationForm을 상속해서 커스터마이징한 폼)
from .forms import SignupForm

# 📌 회원가입 · Signup ===============================================================
def signup(request):
    if request.method == "POST":                    # request가 POST라면
        form = SignupForm(request.POST)             # 사용자가 입력한 데이터를 폼에 바인딩
        if form.is_valid():                         # form의 유효성 검사가 True 이면
            form.save()                             # form 데이터를 auth_user 테이블에 저장
            messages.success(request, "회원가입이 완료되었습니다. 로그인 해주세요.")
                                                    # 성공 메시지를 띄움
            return redirect("accounts:login")       # accounts의 login 페이지로 이동
    else:                                           # POST가 아니라면 = GET 이라면
        form = SignupForm()                         # 회원가입 화면을 구성
    return render(request, "accounts/signup.html",{"form":form})
                                                    # signup.html 템플릿에 form을 전달해서 입력 폼을 렌더링
# 🟢 form.is_valid() :
#       필드 유효성(필수값, 길이 등)
#       비밀번호 정책(settings.py의 validators)
#       password1/password2 일치 여부
#       username 중복 등
# 🟢 form.save() :
#       User 객체 생성
#       비밀번호는 자동 해시 처리
#       DB 저장

# 📌 로그인 · login_view =============================================================
def login_view(request):
    if request.user.is_authenticated:               # True = 이미 로그인한 상태 라면
        return redirect("boards:home")              # boards의 home 페이지로 이동
    
    if request.method == "POST":                    # 요청이 POST 라면
        form = AuthenticationForm(request, data = request.POST)     # 데이터 폼을 매핑
        if form.is_valid():                         # for의 유효성 검사
            user = form.get_user()                  # 검증된 사용자 객체 가져오기
            login(request, user)                    # 세션에 로그인 정보 기록
            return redirect("boards:home")          # boards의 home 페이지로 이동
    else:                                           # POST가 아니다 = GET
        form = AuthenticationForm(request)          # 빈 로그인 폼 생성

    return render(request, "accounts/login.html", {"form":form})    # 최종적으로는 login.html에 form을 전달

# 📌 로그아웃 · logout_view ===========================================================
def logout_view(request):
    logout(request)                                 # 세션에서 사용자 인증 정보 제거 > 즛기 비로그인 상태로 전환
    return redirect("boards:home")                  # home으로 이동