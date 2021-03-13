# 리스트 자료형
odd = [1,3,5,7,9]  # 리스트 안에는 어떠한 자료형도 포함시킬 수 있음
a = list()  # 비어 있는 리스트

# 리스트 인덱싱 (리스트 역시 문자열처럼 인덱싱 적용 가능)
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[3][0])

# 리스트 슬라이싱 (문자열처럼 슬라이싱 기법 적용 가능)
a = [1, 2, 3, 4, 5]
print(a[0:2])
print(a[:2])
print(a[2:])

# 리스트 연산하기 (역시 + 기호 이용해 더할 수 있고 * 기호 사용해 반복 가능)
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)
print(a*3)

# 리스트 길이 구하기
print(len(a))  # len 함수는 문자열, 리스트 외에 튜플, 딕셔너리에서도 사용 가능

# 리스트 수정과 삭제
a = [1, 2, 3]
a[2]=4
print(a)

# del 함수 사용해 리스트 요소 삭제
a = [1, 2, 3]
del a[1]  # del a[x]는 x번째 요소값 삭제. del 함수는 파이썬이 자체적으로 가지고 있는 삭제 함수
print(a)

# 리스트 관련 함수
# 리스트에 요소 추가(append) 리스트 안에는 어떤 자료형도 추가 가능
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5,6])
print(a)

# 리스트 정렬(sort) 리스트 요소 순서대로 정
a = [1, 4, 3, 2]
a.sort()
print(a)

# 리스트 뒤집기(reverse) 리스트를 역순으로 뒤집어 준다(현재 리스트 그대로 거꾸로 뒤집는다)
a = ['a', 'c', 'b']
a.reverse()
print(a)

# 위치 반환(index) find X
a = [1, 2, 3]
print(a.index(3))
# print(a.index(0)) 0은 a 리스트에 존재하지 않기 때문에 값 오류 발생

# 리스트에 요소 삽입(insert) insert(a,b)는 리스트의 a번째 위치에 b를 삽입하는 함수
a = [1, 2, 3]
a.insert(0,4)  # a[0] 위치에 삽입
print(a)
a.insert(3,5)  # a[3] 위치에 삽입
print(a)

# 리스트 요소 제거(remove) 리스트에서 첫 번째로 나오는 x 삭제
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
a.remove(3)
print(a)

# 리스트 요소 끄집어내기(pop) pop()는 리스트의 맨 마지막 요소 돌려주고 그 요소 삭제
a = [1, 2, 3]
a.pop()  # 객체 반환
print(a)
a = [1, 2, 3]
a.pop(1)  # pop(x)는 리스트의 x번째 요소 돌려주고 그 요소 삭제
print(a)

# 리스트에 포함된 요소 x의 개수 세기(count) count(x)는 리스트 안에 x가 몇 개 있는지 조사해 그 개수를 돌려주는 함수
a = [1, 2, 3, 1]
print(a.count(1))

# 리스트 확장(extend) extend(x)에서 x에는 리스트만 올 수 있으며 리스트에 x 리스트를 더한다
a = [1, 2, 3]
b = [6, 7]
a.extend(b)  # a.extend([4, 5])는 a+=[4, 5]와 동일
print(a)

