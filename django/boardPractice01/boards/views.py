from django.shortcuts import render
from django.http import HttpResponse

# 📌 1) 5-3 : 임시 홈 ==============================================
def home(request):
    return render(request, "boards/home.html")