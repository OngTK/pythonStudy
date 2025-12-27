"""

URL 라우팅의 시작점

요청 URL → VIEW(mvc의 Controller)를 연결


URL configuration for practice01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import hello # Import 중요!!!!
from .views import user_list

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("hello/", hello),
    # path("user/",user_list)

    path("", include("main.urls"))
]



