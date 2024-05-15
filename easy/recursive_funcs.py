# Ex. 12.2 point A
class RecFuncs:
    def __init__(self):
        pass

    def gs1(self, n: int):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.gs1(n - 2) + self.gs1(n - 1) + 2


number = int(input("Enter a number please:   "))
rec_func = RecFuncs()
print(rec_func.gs1(number))
