# if문

money = True
if money:
    print("택시")
else:
    print("걷기")

# 조건문 다음에 콜론(:)을 잊지 말자! (while, for, def, class도 마찬가지)
# 비교연산자 : x<y x<y x==y x!=y x>=y x<=y
money = 2000
if money >= 3000:
    print("택시")
else:
    print("걷기")

# and, or, not
money = 2000
card = True
if money >= 3000 or card:
    print("택시")
else:
    print("걷기")

# x in s, x not in s
# x in 리스트, 튜플, 문자열, 딕셔너리
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시")
else:
    print("걷기")
# 조건문에서 아무 일도 하지 않게 설정하고 싶을 때는 pass

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시")
elif card:
    print("택시")
else:
    print("걷기")

# if문 한 줄로 작성
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")

# 조건부 표현식
score = 60
message = "success" if score >= 60 else "failure"
# 조건문 참인 경우 if 조건문 else 조건문 거짓인 경우
