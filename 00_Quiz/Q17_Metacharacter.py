# 기초 메타 문자

import re

p = re.compile("a[.]{3,}b")

print(p.match("acccb"))
print(p.match("a....b"))  # 매치 객체 출력
print(p.match("aaab"))
print(p.match("a.cccb"))
