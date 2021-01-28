# abc.txt의 내용을 역순으로 바꾸어 저장하기

# 파일 불러오기
f = open("/Users/junghoyun/Desktop/python/00_Practice_Quiz/Q08_abc.txt", "r")
lines = f.readlines()  # 모든 줄을 읽는 함수
f.close()

# print(lines) # 주의 : EEE뒤에는 \n이 없다

# 내용을 역순으로 바꾸기
lines.reverse()

# 바꾼 파일 저장하기
f = open("/Users/junghoyun/Desktop/python/00_Practice_Quiz/Q08_abc.txt", "w")
for line in lines:
    line = line.strip()  # EEE뒤에는 줄바꿈 없기때문에 모든 줄의 줄바꿈 문자 제거한 다음,
    f.write(line)
    f.write("\n")  # 줄바꿈 문자 다시 넣어준다
f.close()


# key
# EEE뒤에만 줄바꿈이 없다는 사실에 주의
# reverse 함수 사용
