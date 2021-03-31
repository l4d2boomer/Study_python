# 모듈

# 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일
# 모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일
# 우리는 파이썬으로 프로그래밍을 할 때 굉장히 많은 모듈을 사용
# 다른 사람들이 이미 만들어 놓은 모듈을 사용할 수도 있고 우리가 직접 만들어서 사용 가능

# 모듈 만들기
"""
mod1.py에 아래 내용 작성

def add(a, b):
    return a + b

def sub(a, b): 
    return a-b
"""

import mod1
print(mod1.add(3, 4))
print(mod1.sub(4, 2))
# import는 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러오기 가능
# 파이썬 라이브러리는 파이썬을 설치할 때 자동으로 설치되는 파이썬 모듈

# 모듈 이름 없이 함수 이름만 쓰고 싶을 때는 "from 모듈 이름 import 모듈 함수"를 사용
from mod1 import add
add(3, 4)

# add 함수와 sub 함수를 둘 다 사용하고 싶다면 어떻게 해야 할까? 2가지 방법이 있다.

from mod1 import add, sub # 콤마로 구분하여 필요한 함수를 불러올 수 있다.

from mod1 import * # * 문자를 사용하는 방법이다. 정규 표현식에서 * 문자는 "모든 것"이라는 뜻인데 파이썬에서도 마찬가지 의미로 사용


# if __name__ == "__main__": 의 의미
"""
mod1.py 변경
def add(a, b): 
    return a+b

def sub(a, b): 
    return a-b

print(add(1, 4))
print(sub(4, 2))
"""

import mod1 # 5와 2 출력
# 엉뚱하게도 import mod1을 수행하는 순간 mod1.py가 실행이 되어 결괏값을 출력한다. 우리는 단지 mod1.py 파일의 add와 sub 함수만 사용하려고 했는데 말이다.
# 이러한 문제를 방지하려면 mod1.py 파일을 다음처럼 변경해야 한다.
"""
mod1.py 추가 변경
def add(a, b): 
    return a+b

def sub(a, b): 
    return a-b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
"""
# 중요한 차이점!!
# if __name__ == "__main__"을 사용하면 직접 mod1.py을 실행했을 때는 __name__ == "__main__"이 참이 되어 if문 다음 문장이 수행
# 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 __name__ == "__main__"이 거짓이 되어 if문 다음 문장이 수행되지 않음

# __name__ 변수란?
# 파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름
# 만약 직접 mod1.py 파일을 실행할 경우 mod1.py의 __name__ 변수에는 __main__ 값이 저장
# 하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import 할 경우에는 mod1.py의 __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장


# 클래스나 변수 등을 포함한 모듈
"""
mod2.py에 아래 내용 작성
PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2) 
    
    def add(a, b):
        return a+b
"""
# mod2.py는 클래스, 함수, 변수 등을 모두 포함

import mod2
print(mod2.PI)

a = mod2.Math()
print(a.solv(2))
print(mod2.add(mod2.PI, 4.4))


# 다른 파일에서 모듈 불러오기
# 다른 파이썬 파일에서 이전에 만들어 놓은 모듈을 불러와서 사용하는 방법에 대해 알아보자.
# 여기에서는 조금 전에 만든 모듈인 mod2.py 파일을 다른 파이썬 파일에서 불러와 사용

"""
modtest.py에 아래 내용 작성
import mod2
result = mod2.add(3, 4)
print(result)
"""
# 다른 파이썬 파일에서도 import mod2로 mod2 모듈을 불러와서 사용할 수 있다.
# 정상적으로 실행되기 위해서는 modtest.py 파일과 mod2.py 파일이 동일한 디렉터리에 있어야 한다.


# 모듈을 불러오는 또 다른 방법
# 이번에는 모듈을 저장한 디렉터리로 이동하지 않고 모듈을 불러와서 사용하는 방법에 대해 알아보자.
# 1. sys.path.append(모듈을 저장한 디렉터리) 사용하기
"""
import sys
print(sys.path) # sys.path는 파이썬 라이브러리가 설치되어 있는 디렉터리를 보여 준다.
['', 'C:\\Windows\\SYSTEM32\\python37.zip', 'c:\\Python37\\DLLs', 
'c:\\Python37\\lib', 'c:\\Python37', 'c:\\Python37\\lib\\site-packages']
'''
# 만약 파이썬 모듈이 위 디렉터리에 들어 있다면 모듈이 저장된 디렉터리로 이동할 필요 없이 바로 불러서 사용할 수 있다.
# sys.path에 디렉터리를 추가하면 아무 곳에서나 불러 사용할 수 있다
'''
# sys.path.append("C:/doit/mymod")
# >>> sys.path
# ['', 'C:\\Windows\\SYSTEM32\\python37.zip', 'c:\\Python37\\DLLs', 
# 'c:\\Python37\\lib', 'c:\\Python37', 'c:\\Python37\\lib\\site-packages', 
# 'C:/doit/mymod']
"""

# 2. PYTHONPATH 환경 변수 사용하기
# 모듈을 불러와서 사용하는 또 다른 방법으로는 PYTHONPATH 환경 변수를 사용하는 방법이 있다.
"""
C:\doit>set PYTHONPATH=C:\doit\mymod
C:\doit>python
>>> import mod2
>>> print(mod2.add(3,4))
7
"""
# set 명령어를 사용해 PYTHONPATH 환경 변수에 mod2.py 파일이 있는 C:\doit\mymod 디렉터리를 설정한다.
# 그러면 디렉터리 이동이나 별도의 모듈 추가 작업 없이 mod2 모듈을 불러와서 사용할 수 있다.
