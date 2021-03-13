# 집합 자료형 (파이썬 2.3부터 지원한 자료형으로 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형)
s1 = set([1, 2, 3])
print(s1)
s2 = set("Hello")
print(s2)
# set()의 괄호 안에 리스트를 입력하거나 문자열 입력해 만든다.
s = set()  # 비어 있는 집합 자료형

# 집합 자료형의 특징 - 중복 허용하지 않고 순서가 없다 -> 인덱싱으로 값을 얻을 수 없다
# 중복을 허용하지 않는 set의 특징 때문에 자료의 중복을 제거하기 위한 필터 역할로 종종 사용된다

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = {4, 5, 6, 7, 8, 9}
# 교집합
print(s1&s2)
print(s1.intersection(s2))  # 순서 바꿔도 결과 동일
# 합집합
print(s1|s2)
print(s1.union(s2))  # 순서 바꿔도 결과 동일
# 차집합
print(s1-s2)
print(s2-s1)
print(s1.difference(s2))  # 결괃 동일
print(s2.difference(s1))

# 집합 자료형 관련 함수들
# 값 1개 추가하기(add)
s1 = {1, 2, 3}
s1.add(4)
print(s1)
# 값 여러 개 추가하기(update)
s1 = {1, 2, 3}
s1.update([4, 5, 6])
print(s1)
# 특정 값 제거하기(remove)
s1 = {1, 2, 3}
s1.remove(2)
print(s1)