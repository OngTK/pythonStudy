from django.db import models
from django.contrib.auth.models import User

"""
📌 3단계. A) 카테고리 class 정의 ====================================================
    게시글을 분류하기 위한 카테고리 모델
    예) 자유게시판, 공지사항, Q&A 등
"""
class Category(models.Model):
    # 🟢 속성 ------------------------------------------------
    
    # ▶ 카테고리 명 
    # - max_length=20 : 최대 20자 제한
    # - unique=True   : 동일한 이름의 카테고리 중복 생성 방지
    name = models.CharField(max_length=20, unique=True) 
    
    # 🟢 관리자(admin) 페이지 표시용 메타데이터 -----------------
    class Meta:
        verbose_name = "카테고리"           # 단수 표기
        verbose_name_plural = "카테고리"    # 복수 표기
    
    # 🟢 객체를 문자열로 표현할 때 사용
    # - Django admin, shell, template 등에서 표시됨  ----------
    def __str__(self):
        return self.name

"""
📌 3단계. A) 게시물 class 정의 =======================================================
    게시판의 게시글을 표현하는 모델
"""    
class Post(models.Model):
    # 🟢 속성 ------------------------------------------------
    
    # ▶ 카테고리
    # - Category와 N:1 관계 (하나의 카테고리에 여러 게시글)
    # - on_delete=models.  ** PROTECT **
    #   → 카테고리에 연결된 게시글이 있으면, 해당 카테고리 삭제 자체를 막음 (데이터 무결성 유지)
    # - related_name= ** "posts" **
    #   → category.posts.all() 로 역참조 가능
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="post")
    # ▶ 제목
    title = models.CharField(max_length=200)                
    # ▶ 작성자
    # - User와 N:1 관계
    # - on_delete=models.CASCADE
    #   → 사용자가 삭제되면 해당 사용자의 게시글도 함께 삭제
    # - related_name="posts"
    #   → user.posts.all() 로 해당 유저의 글 목록 조회 가능
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post") 
    # ▶ 내용
    content = models.TextField()                            
    # ▶ 생성일
    # - auto_now_add=True
    #   → 최초 생성 시에만 자동 저장
    created_at = models.DateTimeField(auto_now_add=True)    
    # ▶ 수정일
    # - auto_now=True
    #   → 객체가 save() 될 때마다 자동 갱신
    updated_at = models.DateTimeField(auto_now=True)        
    # ▶ 조회수
    # - PositiveIntegerField : 음수 불가
    # - default=0 : 최초 생성 시 0부터 시작
    view_count = models.PositiveIntegerField(default=0)     
    
    # 🟢 메타 데이터 
    class Meta:
        ordering = ["-id"]              # 최신 글이 먼저 오도록 정렬
        verbose_name = "게시글"
        verbose_name_plural = "게시글"
    
    # 🟢 게시글 객체 문자열 표시
    def __str__(self):
        return self.title
    
    