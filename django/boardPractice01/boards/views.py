from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.db.models import F
"""
🔹 render
    - 템플릿을 HTML로 렌더링하여 HttpResponse로 반환
    - context(dict)를 템플릿에 전달할 수 있음
🔹 get_object_or_404
    - QuerySet 결과가 비어 있으면 404 에러 발생
    - 주로 게시물 조회에서 사용
    - 결과가 1개 이상 → 정상 반 / 결과가 0개 → 404 Not Found
🔹 redirect
    - 다른 URL로 이동시키는 응답
    - POST 요청 처리 후 자주 사용 (PRG 패턴)
    - URL 문자열 또는 URL name 모두 가능
    - 새로고침 시 중복 요청 방지
🔹 HttpResponseForbidden
    - HTTP 403 Forbidden 응답 반환
    - 권한은 있지만 접근이 허용되지 않은 경우 사용
    - 로그인은 했지만 “내 글이 아닌데 수정/삭제 시도” 같은 상황
🔹 login_required
    - 로그인하지 않은 사용자의 접근을 차단
    - 로그인 페이지로 자동 리다이렉트
🔹 F
    - DB 컬럼 값을 기준으로 연산
    - Python 메모리로 가져오지 않고 DB 레벨에서 처리
    - 동시성 문제 방지 (조회수 증가), race condition 회피, 성능 우수
"""

from .forms import PostForm
from .models import Category, Post

# 📌 1단계) 5-3 : 임시 홈 ==============================================================
# def home(request):
#     return render(request, "boards/home.html")

# 📌 3단계) G: 카테고리 + 게시물 목록/상세/작성/수정/삭제 ===================================

# 📌 1. 홈 화면 -----------------------------------------------------
def home(request):
    # [1-1] 전체 카테고리 조회
    # - 홈 화면에서 카테고리 목록 출력용
    categories = Category.objects.all()

    # [1-2] 최신 게시글 10개 조회
    # - select_related:
    #   ForeignKey(Category, User)를 JOIN으로 미리 가져와
    #   템플릿에서 추가 쿼리 발생 방지 (성능 최적화)
    latest_posts = Post.objects.select_related("category", "author")[:10]

    # [1-3] 홈 템플릿 렌더링
    return render(request, "boards/home.html", {
        "categories": categories,
        "latest_posts": latest_posts,
    })

# 📌 2. 게시물 리스트 (카테고리별) ---------------------------------------
def post_list(request, category_id):
    # [2-1] 카테고리 단일 조회
    # - 존재하지 않으면 404 반환
    category = get_object_or_404(Category, id=category_id)

    # [2-2] 해당 카테고리에 속한 게시글 목록 조회
    # - 작성자, 카테고리 정보를 JOIN으로 미리 로딩
    posts = Post.objects.filter(category=category).select_related("author", "category")

    # [2-3] 게시글 목록 페이지 렌더링
    return render(request, "boards/post_list.html", {
        "category": category,
        "posts": posts,
    })

# 📌 3. 게시물 상세 조회 ---------------------------------------------------
def post_detail(request, post_id):
    # [3-1] 게시글 단일 조회
    # - 작성자, 카테고리 정보를 함께 조회
    post = get_object_or_404(
        Post.objects.select_related("author", "category"),
        id=post_id
    )

    # [3-2] 조회수 증가
    # - F 객체 사용 → DB 레벨에서 +1 처리
    # - 동시성 문제(race condition) 방지
    Post.objects.filter(id=post.id).update(
        view_count=F("view_count") + 1
    )

    # [3-3] 상세 페이지 렌더링
    return render(request, "boards/post_detail.html", {"post": post})

# 📌 4. 게시물 등록 ---------------------------------------------------------
@login_required  # 로그인한 사용자만 접근 가능
def post_create(request):
    # [4-1] POST 요청 (글 저장)
    if request.method == "POST":
        # [4-1-1] 사용자 입력 데이터를 Form 객체로 바인딩
        form = PostForm(request.POST)

        # [4-1-2] 입력값 유효성 검사
        if form.is_valid():
            # [4-1-3] commit=False
            # - 아직 DB에 저장하지 않고 객체만 생성
            post = form.save(commit=False)

            # [4-1-4] 작성자 설정 (현재 로그인 사용자)
            post.author = request.user

            # [4-1-5] 게시글 최종 저장
            post.save()

            # [4-1-6] 게시글 상세 페이지로 이동
            return redirect(
                "boards:post_detail",
                post_id=post.id
            )

    # [4-2] GET 요청 (글 작성 폼 표시)
    else:
        # [4-2-1] 빈 Form 생성
        form = PostForm()

    # [4-3] 작성 폼 페이지 렌더링
    return render(request, "boards/post_form.html", {
        "form": form,
        "mode": "create",   # 템플릿에서 작성/수정 구분용
    })

# 📌 5. 게시물 수정 -------------------------------------------------------
@login_required
def post_update(request, post_id):
    # [5-1] 수정 대상 게시글 조회
    post = get_object_or_404(Post, id=post_id)

    # [5-2] 권한 검사
    # - 작성자 본인이 아니고
    # - 관리자(staff)도 아니라면 수정 불가
    if post.author != request.user and not request.user.is_staff:
        return HttpResponseForbidden("수정 권한이 없습니다.")

    # [5-3] POST 요청 (수정 저장)
    if request.method == "POST":
        # [5-3-1] 기존 게시글(instance)에 폼 바인딩
        form = PostForm(request.POST, instance=post)

        # [5-3-2] 유효성 검사
        if form.is_valid():
            # [5-3-3] 수정 내용 저장
            form.save()

            # [5-3-4] 상세 페이지로 이동
            return redirect(
                "boards:post_detail",
                post_id=post.id
            )

    # [5-4] GET 요청 (수정 폼 표시)
    else:
        # [5-4-1] 기존 데이터가 채워진 Form 생성
        form = PostForm(instance=post)

    # [5-5] 수정 페이지 렌더링
    return render(request, "boards/post_form.html", {
        "form": form,
        "mode": "update",
        "post": post,
    })

# 📌 6. 게시물 삭제 ---------------------------------------------------
@login_required
def post_delete(request, post_id):
    # [6-1] 삭제 대상 게시글 조회
    post = get_object_or_404(Post, id=post_id)

    # [6-2] 권한 검사 (작성자 또는 관리자만 가능)
    if post.author != request.user and not request.user.is_staff:
        return HttpResponseForbidden("삭제 권한이 없습니다.")

    # [6-3] POST 요청 시 실제 삭제 수행
    if request.method == "POST":
        # [6-3-1] 게시글 삭제
        post.delete()

        # [6-3-2] 홈 화면으로 이동
        return redirect("boards:home")

    # [6-4] 삭제 확인 페이지 렌더링
    return render(
        request,
        "boards/post_confirm_delete.html",
        {"post": post}
    )
