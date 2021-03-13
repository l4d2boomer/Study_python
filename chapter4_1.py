# 입력값을 가지고 어떤 일을 수행한 다음에 그 결과물을 내어놓는 것이 함수가 하는 일
# "반복적으로 사용되는 가치 있는 부분"을 한 뭉치로 묶어서 "어떤 입력값을 주었을 때 어떤 결과값을 돌려준다"라는 식의 함수로 작성하는 것이 현명

def add(a, b):
    return a + b


a = 3
b = 4
c = add(a, b)
print(c)


# 매개변수는 함수에 입력으로 전달된 값을 받는 변수를 의미하고 인수는 함수를 호출할 때 전달되는 입력값 의미
# 입력값이 없는 함수
def say():
    return "Hi"


a = say()
print(a)


# 결과값이 없는 함수
def add(a, b):
    print(f"{a}, {b}의 합은 {a + b}입니다.")


add(3, 4)


# 입력값도 결과값도 없는 함수
def say():
    print("Hi")


# 매개변수 지정하여 호출하기
def add(a, b):
    return a + b


result = add(b=5, a=3)  # 매개변수를 직접 지정하면 다음과 같이 순서에 상관없이 사용할 수 있음
print(result)


# 입력값이 몇 개가 될지 모를 때는?
def add_many(*args):  # *args처럼 매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아서 튜플로 만들어줌 (*args는 임의로 정한 변수 이름)
    result = 0
    for i in args:
        result = result + i
    return result


print(add_many(1, 2, 3))
print(add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def add_mul(choice, *args):  # 함수의 매개변수로 *args만 사용할 수 있는 것은 아니다
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result


result = add_mul('add', 1, 2, 3, 4, 5)
print(result)
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)


# 키워드 파라미터 **kwargs
def print_kwargs(**kwargs):
    print(kwargs)


# **kwargs처럼 매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고 모든 key=value 형태의 결과값이 그 딕셔너리에 저장
print_kwargs(name='foo', age=5)


# 함수의 결과값은 언제나 하나다
def add_and_mul(a, b):
    return a + b, a * b


def add_and_mul(a, b):
    return a + b
    return a * b  # 함수는 return문을 만나는 순간 결과값을 돌려준 다음 함수를 빠져나간다


# return의 또다른 쓰임새 : 특별한 상황일 때 함수를 빠져나가고 싶다면 return을 단독으로 사용

# 매개변수에 초기값 미리 설정하기
# (name, old, man=True)는 되지만 (name, man=True, old)는 안 된다. 초기화시키고 싶은 매개변수는 항상 뒤쪽에 놓는 것을 잊지 말자
def say_myself(name, old, man=True):  # 미리 값 입력
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


# 함수 안에서 선언한 변수의 효력 범위
a = 1


def vartest(aaa):
    aaa += 1


vartest(a)
print(a)  # 함수 안에서 선언한 매개변수는 함수 안에서만 사용될 뿐 함수 밖에서는 사용되지 않는다. 매우 중요!!

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
a = 1


def vartest(a):
    a += 1
    return a


a = vartest(a)
print(a)

# 2. global 명령어 사용하기
a = 1


def vartest():
    global a  # 외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니므로 가급적 2번째 방법은 피할 것을 권장
    a += 1


vartest()
print(a)

# lambda - 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다. 보통 함수를 한 줄로 간결하게 만들 때 사용
# def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다
add = lambda a, b: a + b
result = add(3, 4)
print(result)
# lambda 예약어로 만든 함수는 return 명령어가 없어도 결과값을 돌려준다
