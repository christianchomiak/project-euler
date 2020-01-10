#!/usr/bin/env python3

# PROBLEM 5
# 2520 is the smallest number that can be divided
# by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?

import sys
import timeit
from euler_common import Prime, is_prime

DEFAULT_INPUT = 20
DEFAULT_NUMBER_OF_TESTS = 100000

def test_solution(input, expected_result):
    result = compute_smallest_evenly_divisible_number(input)
    assert result == expected_result, ' Test FAILED, expected: ' + str(expected_result) + ', got: ' + str(result)

def test_solutions():
    test_solution(10, 2520)
    test_solution(20, 232792560)
    print('All Tests OK')

def time_performance(number_of_tests = DEFAULT_NUMBER_OF_TESTS):
    tests = [(compute_smallest_evenly_divisible_number, "Loop"),
             (compute_smallest_evenly_divisible_number_iterator, "Iterator")]
    print('-- Running %d tests --' % number_of_tests)
    print('-- (Result for each is the total time spent per test) -- ')
    for (test_function, test_name) in tests:
        print('%s = %s ' % (test_name, str(timeit.timeit(test_function, number=number_of_tests))))

def compute_smallest_evenly_divisible_number(ceiling = DEFAULT_INPUT):
    result = 1
    i = 2
    while i <= ceiling:
        if is_prime(i):
            powered_prime = i
            while powered_prime * i <= ceiling:
                powered_prime *= i
            result *= powered_prime
        i += 1
    return result

def compute_smallest_evenly_divisible_number_iterator(ceiling = DEFAULT_INPUT):
    result = 1
    for prime in iter(Prime()):
        if prime > ceiling:
            break
        powered_prime = prime
        while powered_prime * prime <= ceiling:
            powered_prime *= prime
        result *= powered_prime
    return result

def main():
    # Check for any command line argument
    if len(sys.argv) == 1:
        # No argument? Default it!
        result = compute_smallest_evenly_divisible_number(DEFAULT_INPUT)
        print(result)
    else:
        # Even if there are more than one
        # arguments, we only care about the
        # first one, so let's continue.

        if sys.argv[1].isnumeric():
            result = compute_smallest_evenly_divisible_number(int(sys.argv[1]))
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
            print("    arg: The ceiling used by the algorithm. Default: %d" % DEFAULT_INPUT)
            print("    option:")
            print("        --test  : Run the unit tests")
            print("        --time  : Measure the performance of different solutions to the problem")
            print("        --help  : Show this help")
    return

if __name__ == '__main__':
    main()
