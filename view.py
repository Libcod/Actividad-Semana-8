class View:
    def __init__(self):
        print("Enter a option : ")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide")

        self.option = input()
        print("Enter the number 1 :")
        self.num1 = input()
        print("Enter the number 2 :")
        self.num2 = input()