"""
views.py

- 요청 처리 로직
- 가장 많이 작성하는 파일
  
"""
from django.shortcuts import render     # default / 4-5-3
from django.http import HttpResponse    # 4-2-1
from django.http import JsonResponse    # 4-4-1  
from .models import Post                # 6-8

# Create your views here.

# 📌 4-2-1. 첫번째 View 만들기 / 문자열 응답
# >> main/urls.py 에서 연결
def hello(request):
    return HttpResponse("Hello, Django!")

# 📌 4-4. View에서 JSON 응답하기
# 🟢 4-4-1. JSON View 작성
def json_test(request):
    data = {
        "name":"Django",
        "version":6,
        "status":"ok"
    }
    return JsonResponse(data)


# 📌 4-5. HTML 응답을 위한 Template 사용
# 🟢 4-5-3. View에서 Template 렌더링
def index(request):
    # 📌 4-6. Veiw > Template 데이터 전달
    context = {
        "title": "Django Template",
        "count": 3
    }
    return render(request, "main/index.html", context)

# 📌 5-4. View → Template 데이터 전달 실습
# 🟢 5-4-1. View 코드
def list_view(request):
    context = {
        "title": "게시글 목록",
        "posts" : [
            "Django 기초",
            "Template 사용법",
            "Model과 ORM"
        ]
    }
    return render(request, "main/list.html", context)

# 📌 6-8. View에서 ORM 사용
def post_list(request):
    posts = Post.objects.all() #ReadAll

    return render(request, 
                  "main/list.html", 
                  {"post1s" : posts}
                )

# Post.objects.create(
#     title = "첫 글",
#     content="내용"
# )
# Post.objects.all()