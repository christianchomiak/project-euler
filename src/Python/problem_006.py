#!/usr/bin/env python3

# PROBLEM #2
# The sum of the squares of the first ten natural numbers is,
#  1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#  (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence, the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# 
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

import timeit

DEFAULT_INPUT = 100

def time_performance():
    number_of_tests = 100000

    tests = [(compute_diff, "Formula"),
             (compute_diff_high_order, "High Order")]

    print("-- Running %d tests --" % number_of_tests)
    print("-- (Result for each is the total time spent per test) -- ")
    for (test_function, test_name) in tests:
        print("%s = %s " % (test_name, str(timeit.timeit(test_function, number=number_of_tests))))


def compute_sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

def compute_square_of_sum(n):
    sum = (n * (n + 1)) // 2
    return sum * sum

# Similar to compute_sum_of_squares but using high order functions
def compute_sum_of_squares_high_order(n):
    from functools import reduce
    squares = map(lambda x: x * x, range(n + 1))
    return reduce(lambda x, y: x + y, squares)

# Similar to compute_square_of_sum but using high order functions
def compute_square_of_sum_high_order(n):
    from functools import reduce
    sum = reduce(lambda x, y: x + y, range(n + 1))
    return sum * sum

def compute_diff(ceiling = DEFAULT_INPUT):
    sum_of_squares = compute_sum_of_squares(ceiling)
    square_of_sum = compute_square_of_sum(ceiling)
    return square_of_sum - sum_of_squares

def compute_diff_high_order(ceiling = DEFAULT_INPUT):
    sum_of_squares = compute_sum_of_squares_high_order(ceiling)
    square_of_sum = compute_square_of_sum_high_order(ceiling)
    return square_of_sum - sum_of_squares

def main():
    result = compute_diff(DEFAULT_INPUT)
    print(result)

if __name__ == '__main__':
    main()