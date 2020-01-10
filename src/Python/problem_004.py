#!/usr/bin/env python3

# PROBLEM 4
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import sys
import timeit
from euler_common import is_palindrome

DEFAULT_INPUT = 3
DEFAULT_NUMBER_OF_TESTS = 100

def test_solution(input, expected_result):
    result = compute_largest_palindrome(input)
    assert result == expected_result, ' Test FAILED, expected: ' + str(expected_result) + ', got: ' + str(result)

def test_solutions():
    test_solution(2, 9009)
    test_solution(3, 906609)
    print('All Tests OK')

def time_performance(number_of_tests = DEFAULT_NUMBER_OF_TESTS):
    # TODO: Add proper test name here
    tests = [(compute_largest_palindrome, 'Loops')]
    print('-- Running %d tests --' % number_of_tests)
    print('-- (Result for each is the total time spent per test) -- ')
    for (test_function, test_name) in tests:
        print('%s = %s ' % (test_name, str(timeit.timeit(test_function, number=number_of_tests))))

def compute_largest_palindrome(number_of_digits = DEFAULT_INPUT):
    if number_of_digits < 1:
        return None
    largest = 0
    floor = 10**(number_of_digits - 1)
    ceiling = floor * 10
    for i in range(floor, ceiling):
        for j in range(floor, ceiling):
            product = i * j
            if product > largest and is_palindrome(str(product)):
                largest = product
    return largest

def main():
    # Check for any command line argument
    if len(sys.argv) == 1:
        # No argument? Default it!
        result = compute_largest_palindrome(DEFAULT_INPUT)
        print(result)
    else:
        # Even if there are more than one
        # arguments, we only care about the
        # first one, so let's continue.

        if sys.argv[1].isnumeric():
            result = compute_largest_palindrome(int(sys.argv[1]))
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
            print("    arg: Number of digits desired. Default: %d" % DEFAULT_INPUT)
            print("    option:")
            print("        --test  : Run the unit tests")
            print("        --time  : Measure the performance of different solutions to the problem")
            print("        --help  : Show this help")
    return

if __name__ == '__main__':
    main()
