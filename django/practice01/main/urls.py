"""
main app 전용 url 파일
"""
from django.urls import path
from .views import hello, json_test, index

urlpatterns = [
    # 📌 4-2-1. 첫번째 View 만들기
    path("hello/", hello),

    # 📌 4-4. View에서 JSON 응답하기
    # 🟢 4-4-2. URL 추가
    path("json/", json_test),

    # 📌 4-5. HTML 응답을 위한 Template 사용
    # 🟢 4-5-4. URL 추가
    path("", index),
]