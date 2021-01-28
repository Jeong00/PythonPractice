# 모듈 사용 방법 3가지(terminal에서)

# 1.sys 모듈 사용하기
# 다음과 같이 sys.path에 디렉터리를 추가하면 추가한 디렉터리에 있는 모듈을 사용할 수 있게 된다.

# import sys
# sys.path.append("/Users/junghoyun/Desktop/Python_practice/")
# import 모듈명

# 2.PYTHONPATH 환경 변수 사용하기
# 다음처럼 PYTHONPATH 환경 변수에 디렉터리를 저장하면 저장한 디렉터리에 있는 모듈을 사용할 수 있게 된다.

# <터미널에서>
# set.PYTHONPATH=/Users/junghoyun/Desktop/Python_practice/
# python
# >>> import 모듈명

# 3.현재 디렉터리 사용하기
# 파이썬 셸을 모듈이 있는 위치로 이동하여 실행해도 모듈을 사용할 수 있게 된다.
# 왜나하면 sys.path에는 현재 디렉터리인 .이 항상 포함돼 있기 떄문이다.

# cd Desktop
# cd Python_practice
# python
# >>> import 모듈명
