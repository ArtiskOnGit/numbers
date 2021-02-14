from math import factorial, sqrt
import time


class Number():
    def __init__(self, n, runtime=False):
        self.type = None
        self.n = None
        self.change_number(n)
        self.runtime = runtime
        self.start_time = 0
        self.end_time = 1

    def change_number(self, n):
        if type(n) == list:
            self.type = "list"
            ret = n

        elif type(n) == int:
            self.type = "int"
            ret = n

        elif type(n) == str:
            try:
                ret = int(n)
                self.type = "int"
            except ValueError:
                print("not a valid input")
                ret = None

        self.n = ret

    def number_function(self, function):
        if self.n != None:
            if self.runtime:
                self.start_time = time.time()

            if self.type == "int":
                ret = getattr(self, function)(self.n)

            elif self.type == "list":
                if len(self.n) == 1:
                    ret = getattr(self, function)(self.n[0])
                elif len(self.n) > 1:
                    ret = [getattr(self, function)(i) for i in self.n]

            if self.runtime:
                self.end_time = time.time()
                print(f"-----\nTIME ELAPSED : {self.end_time - self.start_time} s\n-----")

            return ret
        else:
            return ("The number is not valid")

    def catalan_number(self, n):
        return factorial(2 * n) // (factorial(n + 1) * factorial(n))

    def prime_number(self, n):
        if n == 1:
            return False
        for i in range(2, round(sqrt(n))):
            if n % i == 0:
                return False
        return True

    def parity(self, n):
        if int(repr(n)[-1]) in [0, 2, 4, 6, 8]:
            return ("even")
        else:
            return ("odd")

    def is_factorial(self, n):
        if n > 1:
            i = 1
            j = 1
            while i < n:
                j += 1
                i = i * j
                if i == n:
                    return f"{j}!"

            return f"{j - 1}! < {n} < {j}!"

        elif n == 0:
            return False
        elif n == 1:
            return "0!"

    def is_perfect_square(self, n):
        return round(sqrt(n)) ** 2 == n

    def is_fibbonaci(self, n):
        if self.is_perfect_square(5 * (n ** 2) + 4) or self.is_perfect_square(5 * (n ** 2) - 4):
            return True
        else:
            return False
