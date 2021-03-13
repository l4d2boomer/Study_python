# 자료형의 값을 저장하는 공간, 변수
a = 1
b = "python"
c = [1, 2, 3]
# C나 Java에서는 변수를 만들 때 자료형을 직접 지정해야 한다. 하지만 파이썬은 변수에 저장된 값을 스스로 판단하여 자료형을 지정

a = [1, 2, 3]
# [1, 2, 3] 값을 가지는 리스트 자료형(객체)이 자동으로 메모리에 생성되고 변수 a는 [1, 2, 3] 리스트가 저장된 메모리의 주소 가르킨다
print(id(a))  # id 함수는 변수가 가리키고 있는 객체의 주소 값을 돌려주는 파이썬 내장 함수

# 리스트 복사하고자 할 때
a = [1, 2, 3]
b = a  # b는 a와 완전히 동일하다고 할 수 있다. [1, 2, 3] 리스트를 참조하는 변수가 1개에서 2개로 늘어났음
print(id(a))
print(id(b))  # id(a)와 id(b)의 값이 동일 -> a가 가리키는 대상과 b가 가리키는 대상이 동일
# 동일한 객체를 가리키고 있는지에 대해서 판단하는 파이썬 명령어 is를 실행하면 역시 True
print(a is b)

a[1] = 4
print(a)
print(b)

# b 변수를 생성할 때 a의 변수의 값을 가져오면서 a와는 다른 주소를 가리키는 방법은 없을까? (2가지)
# 1. [:] 이용
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

# 2. copy 모듈 이용
from copy import copy
b = copy(a)
print(b is a)

# 변수를 만드는 여러 가지 방법
a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a, b] = ['python', 'life']
a = b = 'python'
a = 3
b = 5
print(id(a))
print(id(b))
a, b = b, a  # 당연하지만 주소 값도 바꾼다
print(id(a))
print(id(b))

# 호기심 해결 1
test = [1, 2, 3]
print(id(test))
test.append(4)
print(test)
print(id(test))
# 결론 : append 해도 같은 주소 참조

# 호기심 해결 2
test2 = [1, 2, 3]
print(id(test2))
test2 = [1, 2, 3]
print(id(test2))
# 결론 : 값을 재선언 시 주소값 달라짐

"""
mutable
변경 가능한 객체
객체 값 변경 시 메모리 재할당 없음
set, list, dictionary

>>> mutable1 = ['alpha']
>>> hex(id(mutable1))
'0xc44a80'
>>> mutable1.append('bravo')
>>> hex(id(mutable1))
'0xc44a80' # same!

immutable
변경 불가능한 객체
객체 값 변경 시 메모리 재할당
int, float, string, tuple, bool

>>> immutable1 = 1000 #int
>>> hex(id(immutable1))
'0x1cddce0'
>>> immutable1 += 1
>>> hex(id(immutable1))
'0x1cdde30'
"""

'''
is와 ==의 차이
is는 변수가 같은 Object(객체)를 가리키면 True
==는 변수가 같은 Value(값)을 가지면 True

'is'의 예시
a = [1, 2, 3]
b = a
c = [1, 2, 3]
a is b
True
a is c
False

'=='의 예시
a = [1, 2, 3]
b = a
c = [1, 2, 3]
a == b
True
a == c
True
'''