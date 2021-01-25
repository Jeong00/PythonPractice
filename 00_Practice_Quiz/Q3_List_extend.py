# Q3 리스트 더하기와 extend 함수의 차이점

a = [1, 2, 3]
a = a + [4, 5]
print(id(a))
# 기호(+)를 사용하여 더하면 id 값이 바뀐다.

b = [1, 2, 3]
b.extend([4, 5])
print(id(b))
# extend하면 id 값이 바뀌지 않는다.
