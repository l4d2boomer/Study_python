# for문

"""
for문의 기본 구조
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
"""
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

# marks1.py
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# for문과 continue
# marks2.py
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)

# for문과 range함수
# range(10)는 0부터 10미만의 숫자를 포함하는 range 객체 생성
add = 0
for i in range(1, 11):
    add += 1

print(add)

# marks3.py
marks = [90, 25, 67, 45, 80]
len = len(marks)
for number in range(len):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))

# for와 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=' ')  # 해당 결과값 출력할 때 다음 줄로 넘기지 않고 그 줄에 계속 출력하기 위함
    print('')

# 리스트 내포 사용하기 (리스트 안에 for문 포함)
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)

print(result)

a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

a = [1, 2, 3, 4]
# 리스트 내포 안에 if 조건 사용 가능 [표현식 for 항목 in 반복가능행체 if 조건문]
"""for문 2개 이상 사용도 가능
[표현식 for 항목1 in 반복가능객체1 if 조건문1
      for 항목2 in 반복가능객체2 if 조건문2"""
result = [num * 3 for num in a if num % 2 == 0]
print(result)

result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)
