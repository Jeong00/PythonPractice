# 그루핑
# 휴대폰 뒷 4자리를 ####으로 바꾸는 프로그램을 정규식을 사용하여 작성하시오.

import re

data = """
park 010-9999-9998
kim 010-9909-7789
lee 010-8789-7768
"""

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
print(pat.sub("\g<1>-####", data))
