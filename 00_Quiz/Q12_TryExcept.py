# 오류와 예외처리
# 다음 코드의 실행결과를 예측하고 그 이유에 대해 설명하시오

result = 0
try:
    [1, 2, 3][3]
    "a" + 1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)

# 답 : 7
# 이유 : 1번째가 IndexError이므로 마지막 except로 이동한뒤 그 다음에 있는 finally 실행
