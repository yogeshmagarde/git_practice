s = "Hello, World!"
print(s)

def greet(name):
    return f"Hello, {name}!"


def greet_user(name):
    return f"Hello {name}, welcome to feature branch!"

def add_numbers(a, b):
    return a + b


class Calculator:
    def __init__(self, name):
        self.name = name

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


def greet_user(name):
    return f"Hello {name}, welcome to feature branch!"


if __name__ == "__main__":
    calc = Calculator("Basic Calculator")

    print(greet_user("Yogesh"))
    print("Multiply:", calc.multiply(5, 4))
    print("Divide:", calc.divide(10, 2))