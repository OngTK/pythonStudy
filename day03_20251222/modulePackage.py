# 📌 모듈 · Module ================================================
# - 파이썬 파일(.py)로 작성된 코드 집합
# - 함수, 클래스, 변수 등을 포함할 수 있음
# - 코드 재사용성 향상
# - 표준 라이브러리 및 서드파티 라이브러리 활용 가능
# - 사용자 정의 모듈 생성 가능

# math.py 내의 add 함수 예시

# math.py
def add(a, b):
    return a + b

# main.py에서 math 모듈 사용 예시
# `math.add(3, 5)`  # 결과: 8

# 📌 전체 모듈 import -------------------------
# - 모듈 전체를 불러와서 사용

# import math
# result = math.add(3, 5)  # 결과: 8

# 📌 선택적 모듈 import
# - 모듈에서 특정 함수나 클래스만 불러와서 사용

# from math import add
# result = add(3, 5)  # 결과: 8

# 📌 별칭(alias) 사용 예시
# - 모듈 이름이 길거나 충돌이 예상될 때 별칭 사용
# - as 키워드 활용

# import math as m
# result = m.add(3, 5)  # 결과: 8

# 📌 표준 라이브러리 ---------------------------
# - 파이썬에 기본적으로 포함된 모듈 및 패키지 집합
# - 다양한 기능 제공 (예: 파일 입출력, 데이터 처리, 네트워킹 등)
# - 예: os, sys, math, datetime, json 등

# 수학 : math 
# 운영체제 인터페이스 : os
# 시스템 관련 정보 : sys
# 날짜와 시간 : datetime
# 데이터 직렬화 : json
# 랜덤 값 생성 : random
# 정규 표현식 : re
# 파일 및 디렉토리 경로 조작 : pathlib
# HTTP 통신 : http.client

# 📌 패키지 · Package ==============================================
# - 모듈들을 묶어놓은 디렉토리
# - __init__.py 파일이 포함되어 있어야 패키지로 인식됨

# mypackage/
# ├─ __init__.py
# ├─ calc.py
# └─ utils.py

# - 모듈의 구조화 및 관리 용이
# - 서브패키지 포함 가능
# - 네임스페이스 충돌 방지
# - 예: numpy, pandas, requests 등
# - 사용자 정의 패키지 생성 가능
# - 패키지 설치 및 관리 도구: pip, conda 등

# 📌 사용 예시
# from mypackage import calc
# result = calc.add(3, 5)  # 결과: 8

# 📌 pip =========================================================
# - 파이썬 패키지 관리자
# - 외부 라이브러리 설치 및 관리 도구
# - 패키지 설치, 업그레이드, 제거 기능 제공
# - PyPI(Python Package Index)에서 패키지 검색 및 설치 가능
# - 터미널에 명령어를 입력하여 설치 및 관리

# - 명령어 예시:
#   - 설치: pip install package_name
#   - 업그레이드: pip install --upgrade package_name
#   - 제거: pip uninstall package_name

# - 가상 환경과 함께 사용 권장 (venv, virtualenv 등)

# 📌 가상 환경 · Virtual Environment =============================
# - 독립적인 파이썬 환경을 생성하여 패키지 설치 및 관리
# - 프로젝트별로 서로 다른 패키지 버전 관리 가능
# - 주요 도구: venv, virtualenv, conda 등

# - 가상 환경 생성 예시 (venv):
#   python -m venv myenv
# - 가상 환경 활성화 예시:
#   - Windows: myenv\Scripts\activate
#   - macOS/Linux: source myenv/bin/activate
# - 가상 환경 비활성화:
#   deactivate