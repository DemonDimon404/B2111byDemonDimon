import random

class Letters:
    def __init__(self, letters_set):

        self.letter = random.choice(list(letters_set))

    def write_word(self):
        print(self.letter, end="")

class Word:
    def __init__(self, letter1, letter2, letter3):
        self.letter1 = letter1
        self.letter2 = letter2
        self.letter3 = letter3

    def write_word(self):
        self.letter1.write_word()
        self.letter2.write_word()
        self.letter3.write_word()
        print()


list_of_letters = {
    "a": {1},
    "b": {2},
    "c": {3},
}


letters = Letters(list_of_letters.keys())
word = Word(Letters({"a"}), Letters({"b"}), Letters({"c"}))
word.write_word()

