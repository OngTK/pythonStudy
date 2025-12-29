from django.contrib import admin
from django.urls import path, include

# 📌 include : app을 path에 연결할 수 있게 하는 함수

# 📌 settings : 프로젝트의 전역 설정값(setting.py)에 접근하기 위한 객체
# - 개발/운영 분기 처리
# - 정적 파일, 미디어 파일 경로 설정
from django.conf import settings         

# 📌 sttifc : 개발 서버에서 정적·미디어 파일을 URL로 서빙하기 위한 헬퍼 함수
# - static() => URL 패턴(list)을 생성하여 반환
# - 오직 개발 환경에서만 사용
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('',include('boards.urls'))
]

# 📌DEBUT가 true 일 때 = 개발환경일 때,
# - /media/파일명 요청이 오면,
#       media_root 디렉토리에서 파일을 찾아서 응답
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    