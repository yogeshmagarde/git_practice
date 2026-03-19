s = "Hello, World!"
print(s)

def greet(name):
    return f"Hello, {name}!"


def greet_user(name):
    return f"Hello {name}, welcome to feature branch!"

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    print(greet_user("Yogesh"))
    print("Sum:", add_numbers(10, 20))