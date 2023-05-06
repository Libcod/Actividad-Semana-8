class Model:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.result = 0

    def setNum1(self, num1):
        self.num1 = num1

    def setNum2(self, num2):
        self.num2 = num2

    def getNum1(self):
        return self.num1

    def getResult(self):
        return self.result

    def getNum2(self):
        return self.num2

    def add(self, num1, num2):
        self.result = num1 + num2

    def sub(self, num1, num2):
        self.result = num1 - num2

    def mul(self, num1, num2):
        self.result = num1 * num2

    def div(self, num1, num2):
        self.result = num1 / num2
