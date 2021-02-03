# 전방 탐색
# 긍정형 전방 탐색 기법을 사용하여 .com .net이 아닌 이메일 주소는 제외시키는 정규식을 작성하시오.

import re
p = re.compile(".*[@].*[.](?=com$|net$).*$")

print(p.search("jeong@naver.com"))
print(p.search("ho@hanmail.net"))
print(p.search("yun@naver.co.kr"))
