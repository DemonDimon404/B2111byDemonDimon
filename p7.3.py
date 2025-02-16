
def checker(function):

    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"we have problem: {exc}")
        else:
            print(f"we have success: {result}")

    return checker


@checker
def calculate(excpression):
    return eval(excpression)

calculate = checker(calculate)
calculate("2+2")
