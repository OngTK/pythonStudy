from django.http import JsonResponse

def hello(request):
    return JsonResponse({
        "message" : "Hello, Django"
    })

def user_list(request):
    users = [
        {"name": "Alice", "age": 20},
        {"name": "Bob", "age": 25},
    ]
    return JsonResponse(users, safe=False)