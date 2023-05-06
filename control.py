from model import Model


class Control:
    def calcular(num1, num2, option):
        obj_model = Model()
        obj_model.setNum1(num1)
        obj_model.setNum2(num2)

        num1 = float(obj_model.getNum1())
        num2 = float(obj_model.getNum2())
        option = int(option)

        if option == 1:
            obj_model.add(num1, num2)
        elif option == 2:
            obj_model.sub(num1, num2)
        elif option == 3:
            obj_model.mul(num1, num2)
        elif option == 4:
            obj_model.div(num1, num2)

        print("El resultado es : ", obj_model.getResult())
        return obj_model.getResult()
