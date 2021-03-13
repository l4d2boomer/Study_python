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
type(a)  # 객체 a가 FourCal 클래스의 객체임을 알 수 있음


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

# 일반 함수와는 달리 메서드의 첫 번째 매개변수 self는 특별한 의미 가진다
# a.setdata(4,2)처럼 호출하면 setdata 메서드의 첫 번째 매개변수 self에는 setdata 메서드를 호출한 객체 a가 자동으로 전달된다

