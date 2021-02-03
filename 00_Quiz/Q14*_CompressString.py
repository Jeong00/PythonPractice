# 문자열 압축하기
# 문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시해 문자열을 압축하여 표시하시오.

data = "aaabbcccccca"
data = list(data)

result = []
count = 1
for i, word in enumerate(data):
    if i+1 < len(data):
        next_word = data[i+1]
        if next_word == word:
            count += 1
        else:
            result.append(word)
            result.append(count)
            count = 1
    else:
        result.append(word)
        result.append(count)

print("".join(list(map(str, result))))
