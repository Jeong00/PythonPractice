# DashInsert 함수만들기
# 숫자로 구성된 문자열을 입력받은 뒤, 문자열 안에서 홀수가 연속되면 두 수 사이에 - 를 추가하고, 짝수가 연속되면 * 추가한다.


def DashInsert(num):
    # 문자열 리스트로 나누기
    num = list(str(num))
    # 값 추가를 위한 새 리스트 정의
    result = []
    # 홀수/짝수 구별하기 + 인덱스 필요(연속되는 두 수를 위해) > 인덱스n 설정
    n = 0
    result.append((num[0]))  # 초기 값 추가(반복문 안에 넣으면 n이 커지면서 n+1과 중복됨)
    for i in num:
        number = int(num[n])
        next_number = int(num[n+1])
        if number % 2 == 0 and next_number % 2 == 0:
            result.append("*")
            result.append(next_number)
        elif number % 2 == 1 and next_number % 2 == 1:
            result.append("-")
            result.append(next_number)
        else:
            result.append(next_number)
        n += 1
        if n+1 == len(num):  # n이 커지면 n+1이 리스트 밖으로 벗어남
            break
    # 리스트 > 문자열로 변환(map안쓰고 join만 쓰면 int값 때문에 실행 안됨)
    return "".join(map(str, result))


print(DashInsert(4546793))

# key
# index 설정
# result.append() 조건, 위치
