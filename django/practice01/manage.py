#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

Django 프로젝트를 실행 / 관리하는 진입점
- 서버실행
- 마이그레이션
- 관리자 생성
- 모든 관리 명령의 시작점
>> 수정을 거의 하지 않음!!
"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practice01.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
