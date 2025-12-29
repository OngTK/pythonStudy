"""
2025-12-29
8️⃣ Form & Validation 기초

📌 Django Form
- HTML Form에서 잘못 입력된 값을 검증

- 역할
    - 서버 단 검증
    - 입력 값 정제
    - 에러 메시지 관리
    - Model과의 자연스러운 연동

📌 종류
- Form
    : 순수 입력 폼
- ModelForm
    : Model 기반 폼
"""

# 📌 8-3. ModelForm 만들기
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post                    # 연결할 Model
        fields = ["title", "content"]   # 폼에 노출할 필드
