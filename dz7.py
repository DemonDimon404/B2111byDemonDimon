def calculate(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"error: {e}"


def calculator():
    print("print stop to stop")

    while True:
        expression = input("write here: ")
        if expression.lower() == "stop":
            print("Bye")
            break
        result = calculate(expression)
        print(f"result: {result}")


calculator()