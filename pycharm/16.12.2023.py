class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."


def print_menu():
    print("Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


calc = Calculator()

while True:
    print_menu()
    choice = input("ОТ ОДНОГО ДО 5")

    if choice == "1":
        num1 = float(input("первое число: "))
        num2 = float(input("второе число: "))
        result = calc.add(num1, num2)
        print("Result: ", result)

    elif choice == "2":
        num1 = float(input("первое число: "))
        num2 = float(input("второе число: "))
        result = calc.subtract(num1, num2)
        print("Result: ", result)

    elif choice == "3":
        num1 = float(input("первое число: "))
        num2 = float(input("второе число: "))
        result = calc.multiply(num1, num2)
        print("Result: ", result)

    elif choice == "4":
        num1 = float(input("первое число: "))
        num2 = float(input("второе число: "))
        result = calc.divide(num1, num2)
        print("Result: ", result)

    elif choice == "5":
        print("Выйти из калькуляторо")
        break

    else:
        print("Invalid")