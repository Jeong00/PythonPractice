# 숫자의 총합 구하기

def sum(*num):
    result = 0
    for n in num:
        result += n
    return result


print(sum(1, 2, 3, 4, 5))

# key
# 여러 입력값을 받는 함수의 표시
