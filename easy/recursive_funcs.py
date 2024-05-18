from memory_profiler import profile
from timeit import timeit


# Ex. 12.2
class RecFuncs:
    def __init__(self):
        pass

    def gs1(self, n: int):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.gs1(n - 2) + self.gs1(n - 1) + 2

    def gs2(self, n: int):
        if n == 1:
            return 1.5
        elif n == 2:
            return 1
        return self.gs2(n - 2) + self.gs2(n - 1) - 2

    def gs3(self, n: int):
        if n == 1:
            return -3
        elif n == 2:
            return 1
        return self.gs3(n - 2) * self.gs3(n - 1) - 1

    def gs4(self, n: int):
        if n == 1:
            return -2
        elif n == 2:
            return 2.5
        elif n == 3:
            return 3
        return self.gs4(n - 3) - self.gs4(n - 1)

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

    # rc_factorial_exec_time = timeit(lambda: rec_func.rc_factorial(number), number=1)
    # print(f"Execution time of recursive factorial: {rc_factorial_exec_time}")

    # it_factorial_exec_time = timeit(lambda: rec_func.it_factorial(number), number=1)
    # print(f"Execution time of iterative factorial: {it_factorial_exec_time}")
    print(rec_func.gs4(number))
