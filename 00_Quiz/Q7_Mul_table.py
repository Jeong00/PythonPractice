# 구구단

# 입력값 받아서 변수 설정
num = input("구구단을 출력할 숫자를 입력하세요(1~9): ")
num = int(num)

# 반복문으로 구구단 만들기
for i in range(1, 10):
    print(i*num, end=" ")

# i = 1
# while i <= 9:
#     print(num*i, end=" ")
#     i += 1
