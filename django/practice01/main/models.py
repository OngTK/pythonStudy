"""
models.py
- DB 테이블 정의
- ORM 클래스

2025.12.29
6️⃣ Model & ORM 기초 (DB 다루기)

📌 Model
- 데이터 구조 정의 + DB 테이블 설계
- Python 클래스
- DB 테이블과 1:1 매핑
- SQL을 대신하는 ORM의 핵심

📌 ORM(Object Relational Mapping)
- 객체(Object) ↔ 관계형 DB(Relational DB)를 연결
- SQL을 직접 쓰지 않고 python코드로 DB를 조작

📌 Model → DB 테이블 생성
1. Migragtion 파일 생성
`python mange.py makemigrations`
== Model을 기반으로 테이블을 만들기 위한 설계도 생성

2. DB 반영
`python manage.py migrate`
== 실제 DB에 테이블 생성

3. DB 생성 위치 
`db.sqlite3`

📌 Django ORM 기본 CRUD
🟢 Create

Post.object. create(
    title = "Django ORM",
    content = "ORM 기초 학습"
)

🟢 Read
ReadAll
    Post.object.all()
Read
    Post.object.get(id=1)
Where
    Post.object.filter(title__contains="Django")

🟢 Update
post = Post.objects.get(id=1)   // 수정할 레코드 읽기
post.title = "수정"              // 레코드의 내용 수정
post.save()                     // 저장

🟢 Delete
post = = Post.objects.get(id=1)   // 삭제할 레코드 읽기
post.delete()                     // 삭제하기

📌 Django ORM 실행
`python manage.py shell`

"""

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)    # 짧은 문자열 + max_length : 최대 길이
    content = models.TextField()                # 긴 문자열 필드
    created_at = models.DateTimeField(auto_now_add=True)    # 자동으로 현재시간 삽입하는 날짜/시간 필드
    
