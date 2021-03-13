# 클래스

result = 0


def add(num):
    global result
    result += num
    return result


print(add(3))
print(add(4))
# 이러한 기능을 하는 프로그램이 2대 필요하다면 어떻게 할 것인가?

result1 = 0
result2 = 0


def add1(num):
    global result1
    result1 += num
    return result1


def add2(num):
    global result2
    result2 += num
    return result2


print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))


# 계산기가 3개, 5개, 10개로 점점 더 많이 필요하다면 어떻게 해야 할까? 클래스를 사용하면 간단히 해결 가능
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


# Calculator 클래스로 만든 별개의 계산기 cal1, cal2(파이썬에서는 객체라고 부름)가 각각의 역할 수행
# 계산기의 결과값 역시 다른 계산기의 결과값과 상관없이 독립적인 값 유지
# 계산기 개수가 늘어나더라도 객체를 생성만 하면 되기 때문에 매우 간단

class Cookie:
    pass


a = Cookie()
b = Cookie()


# 클래스로 만든 객체를 인스턴스라고도 한다. a = Cookie() 여기서 a는 객체이고 a 객체는 Cookie의 인스턴스
# 인스턴스라는 말은 특정 객체가 어떤 클래스의 객체인지 관계 위주로 설명할 때 사용. a는 객체 / a는 Cookie의 인스턴스


# 사칙연산 클래스 만들기
# 클래스 구조 만들기
class FourCal:
    pass


a = FourCal()
print(type(a))  # 객체 a가 FourCal 클래스의 객체임을 알 수 있음


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

# 일반 함수와는 달리 메서드의 첫 번째 매개변수 self는 특별한 의미 가진다
# a.setdata(4,2)처럼 호출하면 setdata 메서드의 첫 번째 매개변수 self에는 setdata 메서드를 호출한 객체 a가 자동으로 전달된다

# 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다. 물론 self말고 다른 이름을 사용해도 상관없다.
# 메서드의 첫 번째 매개변수 self를 명시적으로 구현하는 것은 파이썬만의 독특한 특징이다. 예를 들어 자바 같은 언어는 첫 번째 매개변수 self가 필요없다.

# [메서드의 또 다른 호출 방법]
# 잘 사용하지는 않지만 다음과 같이 클래스를 통해 메서드를 호출하는 것도 가능하다.
a = FourCal()
FourCal.setdata(a, 4, 2)
# 위와 같이 클래스 이름.메서드 형태로 호출할 때는 객체 a를 첫 번째 매개변수 self에 꼭 전달해 주어야 한다.
# 반면에 다음처럼 객체.메서드 형태로 호출할 때는 self를 반드시 생략해서 호출해야 한다.
a = FourCal()
a.setdata(4, 2)

# 이제 setdata 메서드의 수행문에 대해 알아보자.
def setdata(self, first, second):   # ① 메서드의 매개변수
    self.first = first              # ② 메서드의 수행문
    self.second = second            # ② 메서드의 수행문
# a.setdata(4, 2)처럼 호출하면 setdata 메서드의 매개변수 first, second에는 각각 값 4와 2가 전달되어 setdata 메서드의 수행문은 다음과 같이 해석된다.
"""
self.first = 4
self.second = 2
self는 전달된 객체 a이므로 다시 다음과 같이 해석된다.

a.first = 4
a.second = 2
a.first = 4 문장이 수행되면 a 객체에 객체변수 first가 생성되고 값 4가 저장된다. 마찬가지로 a.second = 2 문장이 수행되면 a 객체에 객체변수 second가 생성되고 값 2가 저장된다.
"""
# 객체에 생성되는 객체만의 변수를 객체변수라고 부른다.

a = FourCal()
a.setdata(4, 2)
print(a.first)  # 4
print(a.second)  # 2
# a 객체에 객체변수 first와 second가 생성되었음을 확인할 수 있다.

# 이번에는 다음과 같이 a, b 객체를 만들어 보자.
a = FourCal()
b = FourCal()
# 그리고 a 객체의 객체변수 first를 다음과 같이 생성한다.
a.setdata(4, 2)
print(a.first)  # 4
# 이번에는 b 객체의 객체변수 first를 다음과 같이 생성한다.
b.setdata(3, 7)
print(b.first)  # 3
# a 객체의 first 값은 b 객체의 first 값에 영향받지 않고 원래 값을 유지하고 있음을 확인할 수 있다.
# 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다.

# id 함수를 사용하면 객체변수가 독립적인 값을 유지한다는 점을 좀 더 명확하게 증명해 보일 수 있다.
# ※ id 함수는 객체의 주소를 돌려주는 파이썬 내장 함수이다.
a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)
print(id(a.first))   # a의 first 주소값을 확인
# 1839194944
print(id(b.first))   # b의 first 주소값을 확인
# 1839194928
# a 객체의 first 주소 값과 b 객체의 first 주소 값이 서로 다르므로 각각 다른 곳에 그 값이 저장된다는 것을 알 수 있다.
# 객체변수는 그 객체의 고유 값을 저장할 수 있는 공간이다. 객체 변수는 다른 객체들 영향받지 않고 독립적으로 그 값을 유지한다는 점을 꼭 기억하자.

# 다음은 현재까지 완성된 FourCal 클래스이다.
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second


# 더하기 기능 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
a = FourCal()
a.setdata(4, 2) # a객체의 first, second 객체변수에는 각각 값 4와 2가 저장될 것이다.

# 이제 add 메서드를 호출해 보자.
print(a.add())  #6
# 위 내용은 a.add() 메서드 호출 전에 a.setdata(4, 2) 가 먼저 호출되어 a.first = 4, a.second = 2 라고 이미 설정되었기 때문에 다시 다음과 같이 해석한다.
# result = 4 + 2
# 따라서 다음과 같이 a.add()를 호출하면 6을 돌려준다.


# 곱하기, 빼기, 나누기 기능 만들기
# 이번에는 곱하기, 빼기, 나누기 등을 할 수 있게 프로그램을 만들어 보자.
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)
print(a.add())  # 6
print(a.mul())  # 8
print(a.sub())  # 2
print(a.div())  # 2
print(b.add())  # 11
print(b.mul())  # 24
print(b.sub())  # -5
print(b.div())  # 0.375
# 여기까지 사칙연산 기능을 가진 클래스를 만들어 보았다.


# 생성자 (Constructor)
a = FourCal()
# a.add()
# FourCal 클래스의 인스턴스 a에 setdata 메서드를 수행하지 않고 add 메서드를 수행하면 "AttributeError: 'FourCal' object has no attribute 'first'" 오류가 발생한다.
# setdata 메서드를 수행해야 객체 a의 객체변수 first와 second가 생성되기 때문이다.
# 이렇게 객체에 초깃값을 설정해야 할 필요가 있을 때는 setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다는 생성자를 구현하는 것이 안전한 방법이다.
# 중요!! 생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다.
# 파이썬 메서드 이름으로 __init__를 사용하면 이 메서드는 생성자가 된다.
# ※ __init__ 메서드의 init 앞뒤로 붙은 __는 언더스코어(_) 두 개를 붙여 쓴 것이다.
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
# __init__ 메서드는 setdata 메서드와 이름만 다르고 모든 게 동일하다. 단 메서드 이름을 __init__으로 했기 때문에 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출되는 차이가 있다.

# a = FourCal()
# TypeError: __init__() missing 2 required positional arguments: 'first' and 'second'
# a = FourCal()을 수행할 때 생성자 __init__이 호출되어 위와 같은 오류가 발생했다. 오류가 발생한 이유는 생성자의 매개변수 first와 second에 해당하는 값이 전달되지 않았기 때문이다.

# 위 오류를 해결하려면 다음처럼 first와 second에 해당되는 값을 전달하여 객체를 생성해야 한다.
a = FourCal(4, 2)
# ※ __init__ 메서드도 다른 메서드와 마찬가지로 첫 번째 매개변수 self에 생성되는 객체가 자동으로 전달된다는 점을 기억하자.
# 따라서 __init__ 메서드가 호출되면 setdata 메서드를 호출했을 때와 마찬가지로 first와 second라는 객체변수가 생성될 것이다.

a = FourCal(4, 2)
print(a.first)  # 4
print(a.second)  # 2
# add나 div 등의 메서드도 잘 동작하는지 확인해 보자.
a = FourCal(4, 2)
print(a.add())  # 6
print(a.div())  # 2.0
# 이상 없이 잘 동작하는 것을 확인할 수 있다.


# 클래스의 상속
# 상속(Inheritance)이란 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것이다.
# 이번에는 상속 개념을 사용하여 우리가 만든 FourCal 클래스에 ab (a의 b제곱)을 구할 수 있는 기능을 추가해 보자.
# 앞에서 FourCal 클래스는 이미 만들어 놓았으므로 FourCal 클래스를 상속하는 MoreFourCal 클래스는 다음과 같이 간단하게 만들 수 있다.
class MoreFourCal(FourCal):
    pass
# 클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 된다.
# class 클래스 이름(상속할 클래스 이름)
# MoreFourCal 클래스는 FourCal 클래스를 상속했으므로 FourCal 클래스의 모든 기능을 사용할 수 있어야 한다.
a = MoreFourCal(4, 2)
print(a.add())  # 6
print(a.mul())  # 8
print(a.sub())  # 2
print(a.div())  # 2
# 상속받은 FourCal 클래스의 기능을 모두 사용할 수 있음을 확인할 수 있다.

# 왜 상속을 해야 할까?
# 보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다.
# "클래스에 기능을 추가하고 싶으면 기존 클래스를 수정하면 되는데 왜 굳이 상속을 받아서 처리해야 하지?" 라는 의문이 들 수도 있다.
# 하지만 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야 한다.
# 이제 원래 목적인 a의 b제곱(ab)을 계산하는 MoreFourCal 클래스를 만들어 보자.
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.pow())  # 16
# 상속은 MoreFourCal 클래스처럼 기존 클래스(FourCal)는 그대로 놔둔 채 클래스의 기능을 확장시킬 때 주로 사용한다.


# 메서드 오버라이딩
a = FourCal(4, 0)
# a.div()
# FourCal 클래스의 객체 a에 4와 0 값을 설정하고 div 메서드를 호출하면 4를 0으로 나누려고 하기 때문에 위와 같은 ZeroDivisionError 오류가 발생한다.
# 하지만 0으로 나눌 때 오류가 아닌 0을 돌려주도록 만들고 싶다면 어떻게 해야 할까?

# 다음과 같이 FourCal 클래스를 상속하는 SafeFourCal 클래스를 만들어 보자.
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second
# SafeFourCal 클래스는 FourCal 클래스에 있는 div 메서드를 동일한 이름으로 다시 작성하였다.
# 이렇게 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩(Overriding, 덮어쓰기)이라고 한다.
# 이렇게 메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.
# SafeFourCal 클래스에 오버라이딩한 div 메서드는 나누는 값이 0인 경우에는 0을 돌려주도록 수정했다.
# 이제 다시 위에서 수행한 예제를 FourCal 클래스 대신 SafeFourCal 클래스를 사용하여 수행해 보자.

a = SafeFourCal(4, 0)
print(a.div())  # 0
# FourCal 클래스와는 달리 ZeroDivisionError가 발생하지 않고 의도한 대로 0을 돌려주는 것을 확인할 수 있을 것이다.


# 클래스 변수
class Family:
    lastname = "김"
# Family 클래스에 선언한 lastname이 바로 클래스 변수이다. 클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언하여 생성한다.
print(Family.lastname)  # 김
# 클래스 변수는 위 예와 같이 클래스이름.클래스 변수로 사용할 수 있다.
# 또는 다음과 같이 Family 클래스로 만든 객체를 통해서도 클래스 변수를 사용할 수 있다.
a = Family()
b = Family()
print(a.lastname)  # 김
print(b.lastname)  # 김
# 만약 Family 클래스의 lastname을 다음과 같이 "박"이라는 문자열로 바꾸면 어떻게 될까?

Family.lastname = "박"
# 다음과 같이 확인해 보자.
print(a.lastname)  # 박
print(b.lastname)  # 박
# 클래스 변수 값을 변경했더니 클래스로 만든 객체의 lastname 값도 모두 변경된다는 것을 확인할 수 있다.
# 중요!! 즉 클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징이 있다.

# id 함수를 사용하면 클래스 변수가 공유된다는 사실을 증명할 수 있다.
print(id(Family.lastname))  # 4480159136
print(id(a.lastname))  # 4480159136
print(id(b.lastname))  # 4480159136
# id 값이 모두 같으므로 Family.lastname, a.lastname, b.lastname은 모두 같은 메모리를 가리키고 있다.
# 클래스에서 클래스 변수보다는 객체변수가 훨씬 중요하다. 실무 프로그래밍을 할 때도 클래스 변수보다는 객체변수를 사용하는 비율이 훨씬 높다.
