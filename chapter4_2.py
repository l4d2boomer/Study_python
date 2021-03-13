# 사용자 입력과 출력
a = input()
print(a)

number = input("숫자를 입력하세요: ")
print(number)

# print 자세히 알기
# 큰따옴표("")로 둘러싸인 문자열은 + 연산과 동일
print("life" "is" "too short")
print(("life"+"is"+"too short"))
# 문자별 띄어쓰기는 콤마로 한다
print("life", "is", "too short")

# 한 줄에 결과값 출력하기
for i in range(10):
    print(i, end=' ')  # 매개변수 end를 사용해 끝 문자를 지정해야 한다
