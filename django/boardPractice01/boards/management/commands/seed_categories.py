from django.core.management.base import BaseCommand
from boards.models import Category

"""
📌 3단계 - D
    카테고리 4개 시드 넣기
    
📌 커스텀 관리 명령어 클래스
    목적:
    - 게시판에서 사용할 기본 카테고리 데이터를 DB에 한 번에 생성(시드 데이터)하기 위함
    - python manage.py <command명> 으로 실행됨
"""

class Command(BaseCommand):
    # 🟢 커맨드 설명 (python manage.py help 에 표시됨)
    help = "기본 카테골(이슈/정치/취미/자유)를 생성합니다."
    
    
    # 🟢 handle : 실제 커맨드 실행 시 호출되는 메인 메서드
    def handle(self, *args, **options):
        
        # ▶ 생성할 기본 카테고리 이름 목록
        names = ["이슈","정치","취미","자유"]
        # ▶ 새로 생성된 카테고리 개수 카운트
        created = 0
        # ▶ 각 카테고리에 대해
        for name in names:
            # get_or_create:
            # - 동일한 name이 이미 존재하면 기존 객체 반환
            # - 존재하지 않으면 새로 생성
            # - (객체, 생성여부 Boolean) 튜플 반환
            obj, is_created = Category.objects.get_or_create(name=name)

            # 🟢 실제로 새로 생성된 경우만 카운트 증가
            if is_created:
                created += 1

        # 🟢 콘솔 출력 (초록색 SUCCESS 스타일)
        # 예) "카테고리 시드 완료. 새로 생성: 4 개"
        self.stdout.write(
            self.style.SUCCESS(
                f"카테고리 시드 완료. 새로 생성: {created} 개"
            )
        )