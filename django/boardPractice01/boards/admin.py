from django.contrib import admin
from .models import Category, Post  # 모델에서 정의한 카테고리와 게시물을 import

"""
🛠 Django Admin 옵션 설명

- list_display :
  관리자 목록 페이지에서 보여줄 컬럼(필드)들을 지정
  → 여러 객체를 한눈에 비교·관리할 때 사용
  → 모델 필드명 또는 모델 메서드 이름을 튜플로 작성
  예) list_display = ("id", "title", "author", "created_at")

- list_filter :
  관리자 우측 사이드바에 필터 옵션을 생성
  → 특정 조건(카테고리, 날짜, 작성자 등)으로 빠른 필터링 가능
  → ForeignKey, BooleanField, DateField 등에 자주 사용
  예) list_filter = ("category", "created_at")

- search_fields :
  관리자 상단의 검색창에서 검색할 필드를 지정
  → 문자열 기반 검색 (CharField, TextField 위주)
  → ForeignKey는 "__" 문법으로 하위 필드 접근 가능
  예) search_fields = ("title", "content", "author__username")
"""

"""
📌 카테고리
"""
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    
"""
📌 게시물
""" 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "author", "created_at", "view_count")
    list_filter = ("category",)
    search_fields = ("title", "content", "author__username")