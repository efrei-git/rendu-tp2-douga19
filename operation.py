def add(a, b):
        return a + b

def subtract(a, b):
        return a - b

def multiply(a, b):
        return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Division by zero is not allowed")
        return None
