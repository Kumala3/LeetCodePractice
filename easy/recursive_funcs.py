from memory_profiler import profile


# Ex. 12.2
class RecFuncs:
    def __init__(self):
        pass

    def gs1(self, n: int):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.gs1(n - 2) + self.gs1(n - 1) + 2

    def gs2(self, n: int):
        if n == 1:
            return 1.5
        if n == 2:
            return 1
        return self.gs2(n - 2) - self.gs2(n - 1) + 2

    def gs3(self, n: int):
        if n == 1:
            return -3
        if n == 2:
            return 1
        return self.gs3(n - 2) * self.gs3(n - 1) + 2

    # Recursive approach to solve factorial algorithm
    @profile
    def rc_factorial(self, n: int):
        if n == 0:
            return 1
        return n * self.rc_factorial(n - 1)

    # Iterative approach to solve factorial algorithm
    @profile
    def it_factorial(self, n: int):
        result = 1
        if n > 0:
            for i in range(1, n + 1):
                # if i == 0:
                #     break
                result = result * i

        return result


if __name__ == "__main__":
    number = int(input("Enter a number please:   "))
    rec_func = RecFuncs()

    # print(rec_func.gs2(number))
    print(rec_func.rc_factorial(number))
    print(rec_func.it_factorial(number))
