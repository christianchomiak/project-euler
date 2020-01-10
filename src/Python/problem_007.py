#!/usr/bin/env python3

# PROBLEM 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10.001st prime number?

import sys
import timeit
from euler_common import Prime, get_first_n_primes, is_prime

DEFAULT_INPUT = 10001
DEFAULT_NUMBER_OF_TESTS = 10

def test_solution(input, expected_result):
    result = find_nth_prime_number(input)
    assert result == expected_result, ' Test FAILED, expected: ' + str(expected_result) + ', got: ' + str(result)

def test_solutions():
    test_solution(6, 13)
    test_solution(10001, 104743)
    print('All Tests OK')

def time_performance(number_of_tests = DEFAULT_NUMBER_OF_TESTS):
    tests = [(find_nth_prime_number, "Loop"),
             (find_nth_prime_number_list, "List"),
             (find_nth_prime_number_iter, "Iterator")]
    print('-- Running %d tests --' % number_of_tests)
    print('-- (Result for each is the total time spent per test) -- ')
    for (test_function, test_name) in tests:
        print('%s = %s ' % (test_name, str(timeit.timeit(test_function, number=number_of_tests))))

def find_nth_prime_number_iter(n = DEFAULT_INPUT):
    i = 1
    for prime in iter(Prime()):
        if i == n:
            return prime
        i += 1
    return None

def find_nth_prime_number_list(n = DEFAULT_INPUT):
    primes = get_first_n_primes(n)
    return primes[-1] if len(primes) > 0 else None

def find_nth_prime_number(n = DEFAULT_INPUT):
    if n == 0:
        return None
    if n == 1:
        return 2
    latest_prime = 3
    if n > 2:
        for _ in range(3, n + 1):
            current = latest_prime + 2
            while not is_prime(current):
                current += 2
            latest_prime = current
    return latest_prime


def main():
    # Check for any command line argument
    if len(sys.argv) == 1:
        # No argument? Default it!
        result = find_nth_prime_number(DEFAULT_INPUT)
        print(result)
    else:
        # Even if there are more than one
        # arguments, we only care about the
        # first one, so let's continue.

        if sys.argv[1].isnumeric():
            result = find_nth_prime_number(int(sys.argv[1]))
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
            print("    arg: n-th prime position to calculate. Default: %d" % DEFAULT_INPUT)
            print("    option:")
            print("        --test  : Run the unit tests")
            print("        --time  : Measure the performance of different solutions to the problem")
            print("        --help  : Show this help")
    return

if __name__ == '__main__':
    main()
