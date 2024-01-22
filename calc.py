from operation import *

    if __name__ == "__main__":
        while True:
            input_str = input("Enter the calculation (in the format 'num1 operation num2', or 'exit' to exit): ")

            if input_str == "exit":
                break

            num1, operation, num2 = input_str.split()
            num1 = int(num1)
            num2 = int(num2)

            if operation == '+':
                print(num1, "+", num2, "=", add(num1, num2))
            elif operation == '-':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif operation == '*':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif operation == '/':
                result = divide(num1, num2)
                if result is not None:
                    print(num1, "/", num2, "=", result)
            else:
                print("Invalid operation")
