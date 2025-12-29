from django.urls import path
from . import views

# 📌 계정(accounts) 관련된 대표 app name 선언
app_name = 'accounts'

# 📌 계정(accounts) 관련 URL 관리
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]