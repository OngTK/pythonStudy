from django import forms
from .models import Post

"""
📌 게시글(Post) 작성을 위한 ModelForm

    목적:
    - Post 모델과 1:1로 연결된 입력 폼
    - 게시글 생성/수정 화면에서 사용
    - 모델 필드 검증 로직을 자동으로 활용
"""

class PostForm(forms.ModelForm):
    class Meta:
        # 🟢 연결할 모델 -----------------------------------------------------
        # - 이 Form은 Post 모델을 기반으로 생성됨
        model = Post
        
        # 🟢 폼에 노출할 필드 목록 --------------------------------------------
        # - DB 모델의 필드 중 실제로 사용자에게 입력받을 필드만 지정
        # - author, created_at, view_count 등은 서버에서 처리하므로 제외
        fields = ("category", "title", "content")
        
        # 🟢 각 필드별 HTML 위젯 설정 -----------------------------------------
        # - 기본 위젯을 Bootstrap 스타일에 맞게 커스터마이징
        # - attrs를 통해 class, rows 등 HTML 속성 지정 가능
        widgets = {
            # ▶ 제목 입력 필드
            # - TextInput → <input type="text">
            # - class="form-control" → Bootstrap 입력 스타일 적용
            "title": forms.TextInput(attrs={"class": "form-control"}),

            # ▶ 본문 입력 필드
            # - Textarea → <textarea>
            # - rows=10 → 기본 높이 설정
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 10}),

            # ▶ 카테고리 선택 필드
            # - Select → <select>
            # - ForeignKey(Category)를 기반으로 자동 옵션 생성
            # - Bootstrap select 스타일 적용
            "category": forms.Select(attrs={"class": "form-select"}),
        }