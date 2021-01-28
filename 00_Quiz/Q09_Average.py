# 평균값 구하기

# sample.txt값 읽기
f = open("/Users/junghoyun/Desktop/python/00_Practice_Quiz/Q9_sample.txt", "r")
lines = f.readlines()
# 총합 구하기
sum = 0
for line in lines:
    line = line.strip()
    sum += int(line)
f.close()

# 평균 구하기
average = sum / len(lines)

# result.txt에 저장하기
f = open("Q09_result.txt", "w")
f.write(str(average))
f.close()

# key
# readlines() 함수를 사용(평균 구할때 len()함수로 나눠주면 편하기 때문)
# 총합 구할때 반복문, strip()함수 사용 & 리스트 요소는 str값이므로 int로 바꿔서 더함
# result.txt에 저장할때 str값으로 바꿔서 저장
