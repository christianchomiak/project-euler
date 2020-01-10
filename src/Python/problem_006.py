#!/usr/bin/env python3

# PROBLEM 6
# The sum of the squares of the first ten natural numbers is,
#  1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#  (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence, the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# 
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

import sys
import timeit

DEFAULT_INPUT = 100
DEFAULT_NUMBER_OF_TESTS = 100000

def test_solution(input, expected_result):
    result = compute_diff(input)
    assert result == expected_result, ' Test FAILED, expected: ' + str(expected_result) + ', got: ' + str(result)

def test_solutions():
    test_solution(10, 2640)
    test_solution(100, 25164150)
    print('All Tests OK')

def time_performance(number_of_tests = DEFAULT_NUMBER_OF_TESTS):
    tests = [(compute_diff, "Formula"),
             (compute_diff_high_order, "High Order")]
    print('-- Running %d tests --' % number_of_tests)
    print('-- (Result for each is the total time spent per test) -- ')
    for (test_function, test_name) in tests:
        print('%s = %s ' % (test_name, str(timeit.timeit(test_function, number = number_of_tests))))

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

def compute_diff_high_order(ceiling = DEFAULT_INPUT):
    sum_of_squares = compute_sum_of_squares_high_order(ceiling)
    square_of_sum = compute_square_of_sum_high_order(ceiling)
    return square_of_sum - sum_of_squares

def compute_sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

def compute_square_of_sum(n):
    sum = (n * (n + 1)) // 2
    return sum * sum

def compute_diff(ceiling = DEFAULT_INPUT):
    sum_of_squares = compute_sum_of_squares(ceiling)
    square_of_sum = compute_square_of_sum(ceiling)
    return square_of_sum - sum_of_squares

def main():
    # Check for any command line argument
    if len(sys.argv) == 1:
        # No argument? Default it!
        result = compute_diff(DEFAULT_INPUT)
        print(result)
    else:
        # Even if there are more than one
        # arguments, we only care about the
        # first one, so let's continue.

        if sys.argv[1].isnumeric():
            result = compute_diff(int(sys.argv[1]))
            print(result)
        elif sys.argv[1] == "--test":
            test_solutions()
        elif sys.argv[1] == "--time":
            time_performance()
        elif sys.argv[1] != "--help":
                print("Unknown option %s" % sys.argv[1])
                print("usage: %s {[arg]|option}" % sys.argv[0])
                print("Try `%s --help` for more information." % sys.argv[0])
        else:
            print("Usage:")
            print("     %s {[arg]|option}" % sys.argv[0])
            print("Where:")
            print("    arg: The amount of numbers to process. Default: %d" % DEFAULT_INPUT)
            print("    option:")
            print("        --test  : Run the unit tests")
            print("        --time  : Measure the performance of different solutions to the problem")
            print("        --help  : Show this help")
    return

if __name__ == '__main__':
    main()
