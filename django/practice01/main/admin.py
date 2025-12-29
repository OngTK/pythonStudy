"""
admin.py
- 관리자 페이지 설정
"""
from django.contrib import admin
from .models import Post        # 7-4. model 등록

# 📌 7-4. Model을 Admin에 등록
admin.site.register(Post)
    
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)