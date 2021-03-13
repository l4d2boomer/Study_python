# 문자열 자료형

# 문자열 만드는 방법 4가지
str = "Hello World"
str = 'Python is fun'
str = """Hi"""
str = '''Life is too short'''

# 문자열 내에 작은따옴표나 큰따옴표 포함
food = "Python's favorite food is perl"
# food = 'Python's favorite food is perl'' (오류 발생)
say = '"Python is very easy." he says.'
# 백슬래쉬 사용해서 작은따옴표 큰따옴표 포함 (백슬래시를 작은따옴표나 큰따옴표 앞에 삽입 -> 문자 그 자체 의미)
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
# 출력하는 방법을 선택하는 것은 각자의 선택
print(food)
print(say)

# 여러 줄인 문자열을 변수에 대입
multiline = "Life is too short\nYou need python"
print(multiline)  # 단점은 읽기 불편하고 줄이 길어짐

# 위의 단점을 극복하기 위해 작은따옴표 3개나 큰따옴표 3개 사용
multiline='''Life is too short
You need python'''
print(multiline)  # 문자열이 여러 줄인 경우 따옴표 연속해서 쓰는 것이 훨씬 깔끔
# 이스케이프 코드 - 프로그래밍을 할 때 사용할 수 있도록 정의해 둔 문자 조합
# \n : 문자열 안에서 줄 바꿀 때 사용, \t : 문자열 사이에 탭 간격 줄 때 사용 \\ : \ 그대로 표현 \' : ' 그대로 표현 \" : " 그대로 표현

# 문자열 연산
head = "python"
tail = " is fun"
print(head+tail)

#문자열 곱하기
print(head*2)  # 문자열 n번 반복

# 문자열 길이 구하기 (len : 내장 함수)
print(len(head))

# 문자열 인덱싱
a = "Life is too short, You need Python"
print(a[3])  # 파이썬은 0부터 숫자를 센다
print(a[-1])  # 숫자 앞에 마이너스가 있으면 문자열을 뒤에서부터 읽는다

# 문자열 슬라이싱
print(a[0:4])  # 자리 번호 0부터 3까지 -> a[시작 번호:끝 번호]에서 끝 번호는 포함하지 않음 0<=a<4
print(a[19:])  # 시작 번호부터 문자열 끝까지
print(a[:17])  # 처음부터 끝 번호까지
print(a[:])  # 문자열 처음부터 끝까지
print(a[19:-7])  # a[19]부터 a[-8]
# a[1] = 'y' (문자열 자료형은 그 요소값 변경 불가능 -> 슬라이싱 활용해서 새로운 문자열 생성 가능)

# 문자열 포매팅 (문자열 안에 어떤 값 삽입하는 방법)
# 문자열 안에서 숫자를 넣고 싶은 자리에 %d 문자 넣고 삽입할 숫자는 % 문자 다음에 쓴다. (%d는 문자열 포맷 코드)
print("I eat %d apples." % 3)  # 숫자 대입
print("I eat %s apples" % "five")  # 문자열 바로 대입
number = 3
print("I eat %d apples." % number)  # 변수 대입도 가능
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))  # 2개 이상 값 넣을 때는 괄호 안에 콤마로 구분해 값 입력
# %s : 문자열, %c : 문자 1개, %d : 정수, %f : 실수, %o :8진수, %x : 16진수, %% : 문자 % 자체
# 특이한 점은 %s를 사용하면 정수를 넣든 실수를 넣든 자동으로 문자열로 변환시켜줌
print("Error is %d%%" % 98)  # 문자열 포맷 코드와 %가 같은 문자열 안에 존재하는 경우 반드시 %%로 써야 한다

# 포맷 코드와 숫자 함께 사용하기
print("%10s" % "hi")  # %10s는 전체 길이가 10인 문자열 공간에 대입되는 값을 오른쪽 정렬하고 나머지는 공백으로 남겨 둠
print("%-10s" % "hi")  # 왼쪽으로 정렬하고 나머지는 공백
print("%0.4f" % 3.42137234)  # 소수점 네 번째 자리까지만 나타낸다. (반올림)
print("%10.4f" % 3.42137234)  # 소수점 네 번째 자리까지만 표시하고 전체 길이 10인 문자열 공간에서 오른쪽 정렬

# format 함수를 사용한 포매팅
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
print("I eat {0} apples".format(number))
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

# {0}, {1}과 같은 인덱스 항목이 format 함수의 입력값으로 순서에 맞게 바뀜
# 이름으로 넣기 ({name} 형태를 사용할 경우 반드시 name=value와 같은 형태의 입력값이 있어야함)
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
print("I ate {0} apples. so I was sick for {day} days".format(10, day=3))  # 인덱스 항목과 name=value 형태 혼용 가능

print("{0:<10}".format("hi"))  # 왼쪽 정렬
print("{0:>10}".format("hi"))  # 오른쪽 정렬
print("{0:^10}".format("hi"))  # 가운데 정렬
print("{0:=^10}".format("hi"))  # 공백 문자 대신에 지정한 문자 값으로 채워 넣기도 가능 (단, 채워 넣을 문자 값은 정렬 문자 바로 앞에 넣어야 함)
y = 3.42134234
print("{0:0.4f}".format(y))  # 소수점 표현하
print("{0:10.4f}".format(y))  # 자릿수 맞추기 (오른쪽 정렬)
print("{{ and }}".format())  # 중괄호 문자 그대로 사용하고 싶을 경우에는 {{ 와 }}로 표현

# f 문자열 포매팅(파이썬 3.6버젼부터 가능)
name = "홍길동"
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')  # name, age와 같은 변수의 값 참조 가능
print(f'나의 이름은 {name}입니다. 나이는 {age+1}입니다.')
d = {'name': '홍길동', 'age': 30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')  # 딕셔너리도 가능

print(f'{"hi":<10}')  # 왼쪽 정렬
print(f'{"hi":>10}')  # 오른쪽 정렬
print(f'{"hi":^10}')  # 가운데 정렬
print(f'{"hi":=^10}')  # 공백 문자 대체도 가능
print(f'{y:0.4f}')  # 소수점 4번째 자리까지만
print(f'{y:10.4f}')  # 소수점 표현 및 정렬
print(f'{{ and }}')  # 중괄호 문자 그대로 표현


# 문자열 내장 함수 (문자열 변수 이름 뒤에 . 붙인 다음에 함수 이름)
# 문자 개수 세기(count)
a = "hobby"
print(a.count('b'))  # b의 개수

# 위치 알려주기1(find)
a = "Python is the best choice"
print(a.find('b'))  # b가 처음으로 나온 위치 반환
print(a.find('k'))  # 찾는 문자나 문자열 존재하지 않으면 -1 반환

# 위치 알려주기2(index)
a = "Life is too short"
print(a.index('t'))  # t가 처음으로 나온 위치 반환
# print(a.index('k')) 찾는 문자나 문자열이 존재하지 않는다면 오류 발생

# 문자열 삽입(join)
print(",".join('abcd'))  # 문자열의 각각 문자 사이에 '.' 삽입
print(",".join(['a','b','c','d']))  # 문자열뿐만 아니라 리스트나 튜플도 가능

# 대문자화, 소문자화
print("hi".upper())
print("HI".lower())

# 공백 지우기
a = " hi "
print(a.lstrip())  # 왼쪽 공백 지우기
print(a.rstrip())  # 오른쪽 공백 지우기
print(a.strip())  # 양쪽 공백 지우기

# 문자열 바꾸기(replace)
a = "life is too short. life is good"
print(a.replace("life","your leg"))  # 문자열 안의 특정값을 다른 값으로 치환
print(a)  # 원본값 수정 X

# 문자열 나누기(split)
a = "life is too short"
print(a.split())  # 공백 기준으로 문자열 나눔
b = "a:b:c:d"
print(b.split(":"))  # 괄호 안의 값을 구분자로 해서 문자열 나눔
