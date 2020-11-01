class Calculator:
    def __init__(self,result):
        self.result = result

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

c1 = Calculator(5)
print(c1.add(3))
