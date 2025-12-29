from django.urls import path
from . import views

# 📌 게시판(boards) 관련된 대표 app name 선언
app_name = 'boards'

# 📌 게시판(boards) 관련 URL 관리
urlpatterns = [
    path('', views.home, name='home'),  # 임시 홈
]