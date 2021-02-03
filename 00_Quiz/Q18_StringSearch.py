# 문자열 검색
# search는 문자열 전체를 검색하여 정규식과 매치되는지 조사한다(match는 '처음'부터 매치되는지 조사한다)

# match 객체의 메서드
# group : 매치된 문자열을 돌려준다.
# start/end : 매치된 문자열의 시작/끝 위치를 알려준다.
# span : 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.

import re
p = re.compile("[a-z]+")  # 소문자로 이루어진 단어를 뜻한다.
m = p.search("5 python")
print(m.start() + m.end())  # 주의 : 끝 위치는 문자열의 인덱스 + 1 값이다.
