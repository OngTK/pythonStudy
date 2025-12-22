# 📌파일 입출력 · File Input / Output
# 파일 입출력은 프로그램이 외부 파일과 데이터를 주고받는 과정을 의미
# 파이썬에서는 파일 입출력을 위해 내장 함수인 open(), read(), write() 등을 사용
# ⚠️ 파일 입출력 시에는 반드시 파일을 닫아야 함(close())✨✨✨

# 사용 예:
# 로그 파일 저장, 설정 파일 읽기, 데이터 분석 결과 저장,
# CSV/JSON 처리 등 다양한 상황에서 활용

# 📌 파일 열기 · open() ============================================
# 파일이 없으면 새로 생성됨

file = open('example.txt', 'w')  # 쓰기 모드로 파일 열기
file.write('Hello, World!\n')  # 파일에 문자열 쓰기
file.write('This is a test file.\n')
file.close()  # 파일 닫기

# 📌 파일 모드 ==================================================
# 'r' : 읽기 모드 (기본값) - 파일이 존재해야 함
# 'w' : 쓰기 모드 - 파일이 없으면 새로 생성, 있으면 덮어씀
# 'a' : 추가 모드 - 파일이 없으면 새로 생성, 있으면 내용 뒤에 추가
# 'b' : 바이너리 모드 - 이미지, 오디오 등 이진 파일 처리 시 사용
# 't' : 텍스트 모드 (기본값) - 텍스트 파일 처리 시 사용 
# '+' : 읽기/쓰기 모드 - 파일을 읽고 쓸 수 있음
# 'x' : 배타적 생성 모드 - 파일이 존재하면 오류 발생

# 📌 파일 쓰기 · write ==========================================
# 기존 내용 삭제 후 새로 쓰기
file = open('example.txt', 'w')  # 추가 모드로 파일 열기
file.write('Appending a new line.\n')  # 파일에 문자열 추가
file.close()  # 파일 닫기

# 📌 파일 추가 쓰기 · append ====================================
# 기존 내용 뒤에 추가
file = open('example.txt', 'a')  # 추가 모드로 파일 열기
file.write('This line is appended.\n')  # 파일에 문자열 추가
file.close()  # 파일 닫기

# 📌 파일 읽기 · read ==========================================
# 파일 전체 내용 읽기
file = open('example.txt', 'r')  # 읽기 모드로 파일 열기
content = file.read()  # 파일 내용 읽기
print('read 전체 읽기 ===========================')
print(content)  # 읽은 내용 출력
file.close()  # 파일 닫기

# 📌 파일 한 줄씩 읽기 · readline =============================
file = open('example.txt', 'r')  # 읽기 모드로 파일 열기
print('readline 한 줄씩 읽기 ====================')
for line in file:
    print(line.strip())  # 각 줄 출력 (줄바꿈 문자 제거)
file.close()  # 파일 닫기

# 📌 With 문 ✨✨✨ ========================================
# with 블록 안에서 파일을 불러와서 작동 
# 파일 자동 닫기
print('with 문 사용 ===========================')
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # 각 줄 출력 (줄바꿈 문자 제거)
# 파일은 with 블록을 벗어나면 자동으로 닫힘

# 📌 바이너리 파일 읽기 · binary read =======================
# 이미지 파일 등 이진 파일 읽기
print('바이너리 파일 읽기 ====================')
with open('example.txt', 'rb') as file:  # 바이너리 읽기 모드
    binary_content = file.read()
    print(binary_content)  # 바이너리 데이터 출력

# 📌 파일 존재 여부 확인 · os.path ============================
# os.path 모듈 사용
# os.path.exists() 함수로 파일 존재 여부 확인

import os
file_path = 'example.txt'
if os.path.exists(file_path):
    print(f'{file_path} 파일이 존재합니다.')
else:
    print(f'{file_path} 파일이 존재하지 않습니다.')

# 📌 파일 삭제 · os.remove ==================================
# os.remove() 함수로 파일 삭제
if os.path.exists(file_path):
    os.remove(file_path)
    print(f'{file_path} 파일이 삭제되었습니다.')
else:
    print(f'{file_path} 파일이 존재하지 않아 삭제할 수 없습니다.')

# 📌 파일 복사 · shutil ======================================
# shutil 모듈 사용
import shutil
source = 'C:\\Users\\옹태경\\IdeaProjects\\pythonStudy\\day03_20251222\\source.txt'
destination = 'C:\\Users\\옹태경\\IdeaProjects\\pythonStudy\\day03_20251222\\destination.txt'
# 예시로 source.txt 파일 생성
with open(source, 'w') as f:
    f.write('This is the source file.')
shutil.copy(source, destination)
print(f'{source} 파일이 {destination} 위치로 복사되었습니다.')

# 📌 파일 이동 · shutil =====================================
# shutil.move() 함수로 파일 이동
new_location = 'C:\\Users\\옹태경\\IdeaProjects\\pythonStudy\\day03_20251222\\copy\\moved_destination.txt'
shutil.move(destination, new_location)
print(f'{destination} 파일이 {new_location} 위치로 이동되었습니다.')

# 📌 파일 이름 변경 · os.rename ===========================
# os.rename() 함수로 파일 이름 변경
renamed_file = 'C:\\Users\\옹태경\\IdeaProjects\\pythonStudy\\day03_20251222\\copy\\renamed_destination.txt'
os.rename(new_location, renamed_file)
print(f'{new_location} 파일이 {renamed_file} 이름으로 변경되었습니다.')

# 📌 디렉토리 생성 · os.makedirs ========================
# os.makedirs() 함수로 디렉토리 생성
new_dir = 'C:\\Users\\옹태경\\IdeaProjects\\pythonStudy\\day03_20251222\\new_directory'
os.makedirs(new_dir, exist_ok=True)
print(f'{new_dir} 디렉토리가 생성되었습니다.')

# 📌 디렉토리 삭제 · os.rmdir ===========================
# os.rmdir() 함수로 디렉토리 삭제
if os.path.exists(new_dir):
    os.rmdir(new_dir)
    print(f'{new_dir} 디렉토리가 삭제되었습니다.')
else:
    print(f'{new_dir} 디렉토리가 존재하지 않아 삭제할 수 없습니다.')

# 📌 디렉토리 내 파일 목록 조회 · os.listdir ==============
# os.listdir() 함수로 디렉토리 내 파일 및 폴더 목록 조회
current_dir = 'C:\\Users\\옹태경\\IdeaProjects\\pythonStudy\\day03_20251222'
files_and_dirs = os.listdir(current_dir)
print(f'{current_dir} 디렉토리 내 파일 및 폴더 목록:')
for item in files_and_dirs:
    print(item)

# 📌 파일 입출력 예외 처리 · try-except ===================
# try-except 블록으로 파일 입출력 시 발생할 수 있는 예외 처리
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('파일이 존재하지 않습니다. 예외가 처리되었습니다.')
except IOError:
    print('파일 입출력 중 오류가 발생했습니다. 예외가 처리되었습니다.')

