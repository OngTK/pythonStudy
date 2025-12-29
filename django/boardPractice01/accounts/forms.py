from django import forms
# 📌 회원가입용 기본 Form 클래스
from django.contrib.auth.forms import UserCreationForm
# 📌 사용자 user 모델 = auth_user 테이블과 1:1 매핑
from django.contrib.auth.models import User

# 📌 2) 2-2. 회원가입 폼
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")