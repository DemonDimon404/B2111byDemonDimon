import inspect

class Human()
    def __init__(self, age, height, name = 'John'):
        self.age = age
        self.name = name
        self.secondname = 'Wick'

sig = inspect.signature(Human)
for param in sig.parameters.values():