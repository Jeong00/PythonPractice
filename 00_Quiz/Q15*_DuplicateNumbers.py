# 0~9의 문자로 된 숫자를 입력받았을때, 각각 한 번 씩만 사용했는지 확인하기
# 숫자 개수 확인(10개), 중복 확인 필요


def dupnum(data):
    data = list(data)
    if len(data) == 10:
        sdata = set(data)
        if len(sdata) == len(data):
            return True
        else:
            return False
    else:
        return False


print(dupnum("0123456788"))

# key
# 집합(set)으로 중복된 값 제거하기
