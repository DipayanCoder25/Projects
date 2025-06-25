class Reverse:
    def __init__(self, s=""):
        self.s = s

    def get_reversed(self):
        return self.s[::-1]


user_input = input("Enter a word: ")
obj = Reverse(user_input)


print("Reversed word:", obj.get_reversed())

