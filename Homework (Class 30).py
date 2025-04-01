class Reverse:
    def __init__(self, s):
        self.s = s

    def reversed(self):
        return self.s[::-1]

# Usage
obj = Reverse(input("Enter a string: "))
print("Reversed String:", obj.reversed())