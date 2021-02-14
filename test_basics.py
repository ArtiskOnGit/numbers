from unittest import TestCase
from basics import Number

class TestNumber(TestCase):
    def test_number_function(self):
        cat = Number("7594",runtime=True)
        print(cat.number_function("catalan_number"))
        cat.change_number([1,9,8,16,2])
        print(cat.number_function("catalan_number"))

        pri = Number([3319361387],runtime=True)
        print(pri.number_function("prime_number"))
        pri.change_number([50227,80911,81943,26561,10321,75347,53987,31139,54413,39097,1,2])
        print(pri.number_function("prime_number"))

        parity = Number([3319361387],runtime=True)
        print(parity.number_function("parity"))
        parity.change_number([50225,6,1,0,15,98,-7,1,2])
        print(parity.number_function("parity"))

        factorial = Number([479001600], runtime=True)
        print(factorial.number_function("is_factorial"))
        factorial.change_number([50225, 6, 1, 0, 15, 98, -7, 1, 2])
        print(factorial.number_function("is_factorial"))

        p_square = Number([479001600], runtime=True)
        print(p_square.number_function("is_perfect_square"))
        p_square.change_number([2,4,6,9,7,5,10,16])
        print(p_square.number_function("is_perfect_square"))

        is_fibbonaci = Number([479001600], runtime=True)
        print(is_fibbonaci.number_function("is_fibbonaci"))
        is_fibbonaci.change_number([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155])
        print(is_fibbonaci.number_function("is_fibbonaci"))