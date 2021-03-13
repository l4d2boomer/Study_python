# 딕셔너리 자료형

# 딕셔너리는 Key와 Value를 한 쌍으로 갖는 자료형
# 딕셔너리는 리스트나 튜플처럼 순차적으로 해당 요소값을 구하지 않고 Key를 통해 Value 얻는다
dic = {'name': 'pey', 'phone': '011993323', 'birth': '1118'}
# Key에는 변하지 않는 값을 사용하고 Value에는 변하는 값과 변하지 않는 값 모두 사용

# 딕셔너리 쌍 추가, 삭제
# 추가하기
a = {1: 'a'}
a[2] = 'b'
a['name'] = 'pey'
a[3] = [1, 2, 3]
print(a)

# 삭제하기
del a['name']  # del a[key]라고 하면 지정한 Key에 해당하는 {key : value} 쌍 삭제
print(a)

# Key 사용해 Value 얻기 (딕셔너리는 Key 사용해 Value 구하는 방법밖에 없음)
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

# 딕셔너리 만들 때 주의사항
# Key는 고유한 값이므로 중복되는 Key 값을 설정하면 하나 제외한 나머지 것들이 모두 무시된다
a = {1:'a', 1:'b'}
print(a)
# 동일한 Key가 존재하면 어떤 Key에 해당하는 Value를 불러야 할지 알 수 없기 때문이다
# Key에 리스트는 쓸 수 없지만 튜플은 가능(변하는 값인지 변하지 않는 값인지에 달려 있음)

# 딕셔너리 관련 함수
# Key 리스트 만들기(keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())  # dict_keys 객체 반환해준다. 만약에 반환 값으로 리스트가 필요한 경우에는 list(a.keys()) 사용
# dict_keys, dict_values, dict_items 등은 리스트로 변환하지 않아도 반복 구문에 실행 가능
# dict_keys 객체는 리스트를 사용하는 것과 차이가 없지만 리스트 고유의 append, insert, pop, remove, sort 함수 수행 불가능

# Value 리스트 만들기(values)
print(a.values())

# Key, Value 쌍 얻기(items) items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 반환
print(a.items())

# Key, Value 쌍 모두 지우기(clear) clear 함수는 딕셔너리 내 모든 요소 삭제. 빈 딕셔너리는 {}로 표현
a.clear()

# Key로 Value 얻기(get)
# a.get('name')은 a['name]과 동일한 결과값 돌려받지만 존재하지 않는 키로 값을 가져오려고 할 경우 None을 반환
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))
print(a.get('nokey'))  # None 반환
print(a.get('foo', 'bar'))  # Key 값이 없을 경우 미리 정해 둔 값으로 대신 가져오게 할 수 있음

# 해당 Key가 딕셔너리 안에 있는지 조사(in)
print('name' in a)
print('email' in a)
