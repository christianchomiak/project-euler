#!/usr/bin/env python3

# PROBLEM 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import sys
import timeit
from euler_common import Prime, is_prime

DEFAULT_INPUT = 600851475143

def test_solution(input, expected_result):
    result = find_largest_prime_factor_alt(input)
    assert result == expected_result, " Test FAILED, expected: " + str(expected_result) + ", got: " + str(result)

def test_solutions():
    test_solution(13195, 29)
    test_solution(600851475143, 6857)
    print("All Tests OK")

def find_largest_prime_factor(number = DEFAULT_INPUT):
    if is_prime(number):
        return number
    largest = 1
    i = 2
    while i * i <= number:
        if number % i == 0 and is_prime(i):
            largest = i
        i += 1
    return largest

def find_largest_prime_factor_alt(number = DEFAULT_INPUT):
    largest = 1
    for prime in iter(Prime()):
        if prime * prime > number:
            break
        if number % prime == 0:
            largest = prime
    return largest

def time_performance():
    number_of_tests = 2

    tests = [(find_largest_prime_factor, "Loop"),
             (find_largest_prime_factor_alt, "Loop + Iterator")]

    print("-- Running %d tests --" % number_of_tests)
    print("-- (Result for each is the total time spent per test) -- ")
    for (test_function, test_name) in tests:
        print("%s = %s " % (test_name, str(timeit.timeit(test_function, number=number_of_tests))))

def main():
    # Check for any command line argument
    if len(sys.argv) == 1:
        # No argument? Default it!
        number = DEFAULT_INPUT
    else:
        # Even if there are more than one
        # arguments, we only care about the
        # first one, so let's continue.

        if sys.argv[1].isnumeric():
            number = int(sys.argv[1])
        elif sys.argv[1] == '--test':
            test_solutions()
            return
        elif sys.argv[1] == '--time':
            time_performance()
            return
        elif sys.argv[1] != '--help':
                print("Unknown option %s" % sys.argv[1])
                print("usage: %s {[arg]|option}" % sys.argv[0])
                print("Try `%s --help' for more information." % sys.argv[0])
                return
        else:
            print("Usage:")
            print("     %s {[arg]|option}" % sys.argv[0])
            print("Where:")
            print("    arg: The number whose largest prime factor will be calculated. Default: %d" % DEFAULT_INPUT)
            print("    option:")
            print("        --test  : Run the unit tests")
            print("        --time  : Measure the performance of different solutions to the problem")
            print("        --help  : Show this help")
            return
    result = find_largest_prime_factor(number)
    print(result)

if __name__ == '__main__':
    main()