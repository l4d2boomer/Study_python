# 파일 읽고 쓰기

# 파일 생성하기
"""
f = open("새파일.txt", 'w')
f.close()
"""
# 파일 생성하기 위해 파이썬 내장 함수 open 사용 ("파일 이름", "파일 열기 모드"를 입력값으로 받고 결과값으로 파일 객체를 돌려줌)
# r : 읽기모드, w : 쓰기모드, a : 추가모드(파일의 마지막에 새로운 내용을 추가시킬 때 사용)
# 해당 파일이 이미 존재할 때 쓰기 모드로 열면 원래 내용은 모두 사라지고, 해당 파일이 없다면 새로운 파일 생성
# f = open("C:\doit\새파일.txt",'w')
# f.close()는 파일 객체를 닫아주는 역할 (사실 생략해도 무방, 프로그램 종료 시 파이썬 프로그램이 열려 있는 파일 객체 자동으로 닫아주므로)
# 다만 쓰기모드로 열었던 파일을 닫지 않고 다시 사용하려고 오류가 발생하므로 close() 사용해서 미리 닫아주는 것을 권장

# 파일을 쓰기 모드로 열어 출력값 적기
"""
f = open("C:\\doit\\새파일.txt", 'w')
for i in range(1, 11):
    data = f"{i}번째 줄입니다"
    f.write(data)
f.close()
"""

# 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
# readline() 함수 이용하기
"""
f = open("C:\\doit\\새파일.txt", 'r')
line = f.readline()  # 파일의 첫 번째 줄을 읽어 출력
print(line)
f.close()
"""

"""
f = open("C:\\doit\\새파일.txt", 'r')
while True:
    line = f.readline()  # 무한 루프 안에서 파일을 계속해서 한 줄씩 읽어 들이다가 더 이상 읽을 줄이 없으면 break 수행
    if not line: break
    print(line)
f.close()
"""

# readlines 함수 이용하기
"""
f = open("C:\\doit\\새파일.txt", 'r')
lines = f.readlines()  # 파일의 모든 줄을 읽어 각각의 줄을 요소로 가진 리스트 반환
for line in lines:
    print(line)
f.close()
"""

# read 함수 이용하기
"""
f = open("C:\\doit\\새파일.txt", 'r')
data = f.read()
print(data)
f.close()
"""

# 파일에 새로운 내용 추가하기
"""
f = open("C:\\doit\\새파일.txt", 'a')
for i in range(11, 20):
    data = f"{i}번째 줄입니다"
    f.write(data)
f.close()
"""

# with문과 함께 사용
"""
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
"""
# with문을 사용하면 with 블록을 벗어나는 순간 파일 객체 f가 자동으로 closee되어 편리

# sys 모듈로 매개변수 주기
"""
import sys

args = sys.argv[1:]  # argv는 명령 창에서 입력한 인수 의미 (띄어쓰기로 구분)
for i in args:
    print(i)
"""
# C:\doit>python sys1.py aaa bbb ccc로 입력하면
# aaa
# bbb
# ccc
