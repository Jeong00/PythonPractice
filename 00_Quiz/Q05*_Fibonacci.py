# 피보나치 함수

# 첫번째 항 = 0, 두번째 항 = 1 / 입력을 정수 n으로 받으면 > n 이하까지 출력
# 첫번째 항과 두번째 항을 더한 값이 다음 항이라는 것을 어떻게 표현해야하나?

# input값을 입력으로 하는 함수 만들기
n = input("피보나치 수열을 출력할 값을 입력하세요: ")
n = int(n)


# 첫번째 항과 두번째 항을 먼저 정의
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
# 재귀함수를 활용해서 fibo(n) 정의
    if n > 1:
        return fibo(n-2) + fibo(n-1)


# 반복문으로 앞의 값 모두 표시
i = 0
while i <= n:
    print(fibo(i), end=" ")
    i += 1

# key
# 1. 재귀함수의 활용
# 2. input으로 받은 값을 변수로 설정해 함수의 입력값으로 넣기, 반복문에 앞에서 설정한 변수 사용하기

# 풀이2
# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     if n > 1:
#         return fibo(n-2) + fibo(n-1)


# for i in range(1, 5):
#     print(fibo(i), end=" ")
