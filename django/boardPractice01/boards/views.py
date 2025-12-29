from django.shortcuts import render
from django.http import HttpResponse

# 📌 1) 5-3 : 임시 홈 ==============================================
def home(request):
    return HttpResponse("Django Board Pracite Home")