from tkinter import *
from control import Control


class View:
    def __init__(self):
        obj_control = Control
        raiz = Tk()
        window = Frame(raiz, width=600, height=300)
        window.pack()

        num1Label = Label(window, text="Numero 1").place(x=30, y=70)
        num1Label = Label(window, text="Numero 2").place(x=330, y=70)
        resultLabel = Label(window, text="Result : ").place(x=100, y=150)

        num1Input = Entry(window)
        num1Input.place(x=100, y=70)
        num2Input = Entry(window)
        num2Input.place(x=400, y=70)

        option = IntVar()

        Radiobutton(window, text="add", variable=option, value=1).place(x=100, y=30)
        Radiobutton(window, text="sub", variable=option, value=2).place(x=200, y=30)
        Radiobutton(window, text="mul", variable=option, value=3).place(x=300, y=30)
        Radiobutton(window, text="div", variable=option, value=4).place(x=400, y=30)

        def executeCalculate():
            resultado = ""
            resultado = obj_control.calcular(num1Input.get(), num2Input.get(), option.get())
            Label(window, text=resultado).place(x=220, y=150)

        Button(window, text="Calcular", command=executeCalculate).place(x=350, y=200)

        raiz.mainloop()

        # print("Enter a option : ")
        # print("1. Add")
        # print("2. Substract")
        # print("3. Multiply")
        # print("4. Divide")
        #
        # self.option = input()
        # print("Enter the number 1 :")
        # self.num1 = input()
        # print("Enter the number 2 :")
