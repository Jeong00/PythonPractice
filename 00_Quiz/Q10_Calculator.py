# 사칙연산 계산기

# 생성자를 통해 클래스에서 값 받기
class Calculator:
    def __init__(self, num_list):
        self.num_list = num_list

    def sum(self):
        result = 0
        for num in self.num_list:
            result += num
        return result

    def avg(self):
        result = 0
        for num in self.num_list:
            result += num
        average = result / len(self.num_list)
        return average


cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg())


# key
# 생성자(__init__)의 이해
