# 내장 함수

# 라이브러리를 살펴보기 전에 파이썬 내장 함수를 먼저 살펴보자. 이러한 파이썬 내장 함수는 외부 모듈과 달리 import가 필요하지 않기 때문에 아무런 설정 없이 바로 사용할 수 있다.
# 활용 빈도가 높고 중요한 함수를 중심으로 알파벳 순서대로 간략히 정리했다.


# abs
# abs(x)는 어떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 돌려주는 함수이다.
print(abs(3))
print(abs(-3))
print(abs(-1.2))


# all
# all(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다.
# ※ 반복 가능한 자료형이란 for문으로 그 값을 출력할 수 있는 것을 의미한다. 리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다.
print(all([1, 2, 3]))
# 리스트 자료형 [1, 2, 3]은 모든 요소가 참이므로 True를 돌려준다.

print(all([1, 2, 3, 0]))
# 리스트 자료형 [1, 2, 3, 0] 중에서 요소 0은 거짓이므로 False를 돌려준다.

print(all([]))  # True
# 만약 all의 입력 인수가 빈 값인 경우에는 True를 리턴한다.


# any
# any(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x의 요소 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때에만 False를 돌려준다. all(x)의 반대이다.

print(any([1, 2, 3, 0]))
# 리스트 자료형 [1, 2, 3, 0] 중에서 1, 2, 3이 참이므로 True를 돌려준다.

print(any([0, ""]))
# 리스트 자료형 [0, ""]의 요소 0과 ""은 모두 거짓이므로 False를 돌려준다.

print(any([]))
# 만약 any의 입력 인수가 빈 값인 경우에는 False를 리턴한다.


# chr
# chr(i)는 아스키(ASCII) 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이다.
# ※ 아스키 코드란 0에서 127 사이의 숫자를 각각 하나의 문자 또는 기호에 대응시켜 놓은 것이다.

print(chr(97))  # 'a'
print(chr(48))  # '0'


# dir
# dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다.

print(dir([1, 2, 3]))  # ['append', 'count', 'extend', 'index', 'insert', 'pop',...]
print(dir({'1':'a'}))  # ['clear', 'copy', 'get', 'has_key', 'items', 'keys',...]


# divmod
# divmod(a, b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.

print(divmod(7, 3))  # (2, 1)


# enumerate
# enumerate는 "열거하다"라는 뜻이다. 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
# ※ 보통 enumerate 함수는 다음 예제처럼 for문과 함께 자주 사용한다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
# 0 body
# 1 foo
# 2 bar
# 순서 값과 함께 body, foo, bar가 순서대로 출력되었다. 즉 위 예제와 같이 enumerate를 for문과 함께 사용하면 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다.
# for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려 주는 인덱스 값이 필요할때 enumerate 함수를 사용하면 매우 유용하다.


# eval
# eval(expression )은 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수이다.

print(eval('1+2'))  # 3
print(eval("'hi' + 'a'"))  # 'hia'
print(eval('divmod(4, 3)'))  # (1, 1)
# 보통 eval은 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용한다.


# filter
# filter란 무엇인가를 걸러낸다는 뜻으로 filter 함수도 동일한 의미를 가진다.
# filter 함수는 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다.
# 그리고 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서(걸러 내서) 돌려준다.
def positive(l): 
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result
print(positive([1,-3,2,0,-5,6]))  # 결과값: [1, 2, 6]
# 즉 위에서 만든 positive 함수는 리스트를 입력값으로 받아 각각의 요소를 판별해서 양수 값만 돌려주는 함수이다.

# filter 함수를 사용하면 위 내용을 다음과 같이 간단하게 작성할 수 있다.
def positive(x):
    return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))  # 결과값: [1, 2, 6]
# 여기에서는 두 번째 인수인 리스트의 요소들이 첫 번째 인수인 positive 함수에 입력되었을때 반환 값이 참인 것만 묶어서 돌려준다.
# 앞의 예에서는 1, 2, 6만 양수여서 x > 0 문장이 참이되므로 [1, 2, 6]이라는 결괏값을 돌려주게 된 것이다.

# 앞의 함수는 lambda를 사용하면 더욱 간편하게 코드를 작성할 수 있다.
list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))  # [1, 2, 6]


# hex
# hex(x)는 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려주는 함수이다.
print(hex(234))  # '0xea'
print(hex(3))  # '0x3'


# id
# id(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수이다.
a = 3
print(id(3))  # 135072304
print(id(a))  # 135072304
b = a
print(id(b))  # 135072304
# 위 예의 3, a, b는 고유 주소 값이 모두 135072304이다. 즉 3, a, b가 모두 같은 객체를 가리키고 있다.
# 만약 id(4)라고 입력하면 4는 3, a, b와 다른 객체이므로 당연히 다른 고유 주소 값이 출력된다.
print(id(4))  # 135072292


# input
# input([prompt])은 사용자 입력을 받는 함수이다. 매개변수로 문자열을 주면 다음 세 번째 예에서 볼 수 있듯이 그 문자열은 프롬프트가 된다.
a = input()
b = input("Enter: ")


# int
# int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로, 정수를 입력으로 받으면 그대로 돌려준다.
print(int('3'))  # 3
print(int(3.4))  # 3

# int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려준다.
# 2진수로 표현된 11의 10진수 값은 다음과 같이 구한다.
print(int('11', 2))  # 3
# 16진수로 표현된 1A의 10진수 값은 다음과 같이 구한다.
print(int('1A', 16))  # 26


# isinstance
# isinstance(object, class)는 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.
class Person: pass
a = Person()
print(isinstance(a, Person))  # True

b = 3
print(isinstance(b, Person))  # False


# len
# len(s)은 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수이다.

print(len("python"))  # 6
print(len([1,2,3]))  # 3
print(len((1, 'a')))  # 2


# list
# list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.
print(list("python"))  # ['p', 'y', 't', 'h', 'o', 'n']
print(list((1,2,3)))  # [1, 2, 3]

# list 함수에 리스트를 입력으로 주면 똑같은 리스트를 복사하여 돌려준다.
a = [1, 2, 3]
b = list(a)
print(b)  # [1, 2, 3]


# map
# map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result
result = two_times([1, 2, 3, 4])
print(result)  # 결과값: [2, 4, 6, 8]

# 위 예제는 map 함수를 사용하면 다음처럼 바꿀 수 있다.

def two_times(x):
    return x*2
print(list(map(two_times, [1, 2, 3, 4])))  # [2, 4, 6, 8]

# 앞의 예는 lambda를 사용하면 다음처럼 간략하게 만들 수 있다.
print(list(map(lambda a: a*2, [1, 2, 3, 4])))  # [2, 4, 6, 8]


# max
# max(iterable)는 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수이다.

print(max([1, 2, 3]))  # 3
print(max("python"))  # 'y'

# min
# min(iterable)은 max 함수와 반대로, 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수이다.

print(min([1, 2, 3]))  # 1
print(min("python"))  # 'h'


# oct
# oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수이다.
print(oct(34))  # '0o42'
print(oct(12345))  # '0o30071'


# open
# open(filename, [mode])은 "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를 돌려주는 함수이다. 읽기 방법(mode)을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다.
# mode	설명
# w	쓰기 모드로 파일 열기
# r	읽기 모드로 파일 열기
# a	추가 모드로 파일 열기
# b	바이너리 모드로 파일 열기 (b는 w, r, a와 함께 사용한다.)

# f = open("binary_file", "rb")
# rb는 "바이너리 읽기 모드"를 의미한다.

# 다음 예의 fread와 fread2는 동일한 방법이다.
# fread = open("read_mode.txt", 'r')
# fread2 = open("read_mode.txt")
# 즉 모드 부분을 생략하면 기본값으로 읽기 모드 r를 갖게 된다.

# 다음은 추가 모드(a)로 파일을 여는 예이다.
# fappend = open("append_mode.txt", 'a')


# ord
# ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다.
# ※ ord 함수는 chr 함수와 반대이다.
print(ord('a'))  # 97
print(ord('0'))  # 48


# pow
# pow(x, y)는 x의 y 제곱한 결괏값을 돌려주는 함수이다.
print(pow(2, 4))  # 16
print(pow(3, 3))  # 27


# range
# range([start,] stop [,step] )는 for문과 함께 자주 사용하는 함수이다. 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.

# 인수가 하나일 경우
# 시작 숫자를 지정해 주지 않으면 range 함수는 0부터 시작한다.
print(list(range(5)))  # [0, 1, 2, 3, 4]

# 인수가 2개일 경우
# 입력으로 주어지는 2개의 인수는 시작 숫자와 끝 숫자를 나타낸다. 단 끝 숫자는 해당 범위에 포함되지 않는다는 것에 주의하자.
print(list(range(5, 10)))  # [5, 6, 7, 8, 9]

# 인수가 3개일 경우
# 세 번째 인수는 숫자 사이의 거리를 말한다.
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]
print(list(range(0, -10, -1)))  # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]


# round
# round(number[, ndigits]) 함수는 숫자를 입력받아 반올림해 주는 함수이다.
# ※ [, ndigits]는 ndigits가 있을 수도 있고 없을 수도 있다는 의미이다.
print(round(4.6))  # 5
print(round(4.2))  # 4

# 다음과 같이 실수 5.678을 소수점 2자리까지만 반올림하여 표시할 수 있다.
print(round(5.678, 2))  # 5.68
# round 함수의 두 번째 매개변수는 반올림하여 표시하고 싶은 소수점의 자릿수(ndigits)이다.


# sorted
# sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.
print(sorted([3, 1, 2]))  # [1, 2, 3]
print(sorted(['a', 'c', 'b']))  # ['a', 'b', 'c']
print(sorted("zero"))  # ['e', 'o', 'r', 'z']
print(sorted((3, 2, 1)))  # [1, 2, 3]
# 리스트 자료형에도 sort 함수가 있다. 하지만 리스트 자료형의 sort 함수는 리스트 객체 그 자체를 정렬만 할 뿐 정렬된 결과를 돌려주지는 않는다.


# str
# str(object)은 문자열 형태로 객체를 변환하여 돌려주는 함수이다.
print(str(3))  # '3'
print(str('hi'))  # 'hi'
print(str('hi'.upper()))  # 'HI'


# sum
# sum(iterable) 은 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수이다.
print(sum([1,2,3]))  # 6
print(sum((4,5,6)))  # 15


# tuple
# tuple(iterable)은 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다. 만약 튜플이 입력으로 들어오면 그대로 돌려준다.
print(tuple("abc"))  # ('a', 'b', 'c')
print(tuple([1, 2, 3]))  # (1, 2, 3)
print(tuple((1, 2, 3)))  # (1, 2, 3)


# type
# type(object)은 입력값의 자료형이 무엇인지 알려 주는 함수이다.

print(type("abc"))  # <class 'str'>
print(type([ ]))  # <class 'list'>
print(type(open("test", 'w'))) # <class '_io.TextIOWrapper'>


# zip
# zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
# ※ 여기서 사용한 *iterable은 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있다는 의미이다.
print(list(zip([1, 2, 3], [4, 5, 6])))  # [(1, 4), (2, 5), (3, 6)]
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip("abc", "def")))  # [('a', 'd'), ('b', 'e'), ('c', 'f')]
