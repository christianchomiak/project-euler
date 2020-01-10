#!/usr/bin/env python3

# PROBLEM 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import sys
import timeit
from euler_common import Prime, is_prime, get_first_n_primes

DEFAULT_INPUT = 2000000
DEFAULT_NUMBER_OF_TESTS = 1

def test_solution(input, expected_result):
    result = sum_prime_numbers_up_to_n(input)
    assert result == expected_result, ' Test FAILED, expected: ' + str(expected_result) + ', got: ' + str(result)

def test_solutions():
    test_solution(10, 17)
    test_solution(2000000, 142913828922)
    print('All Tests OK')

def time_performance(number_of_tests = DEFAULT_NUMBER_OF_TESTS):
    tests = [(sum_prime_numbers_up_to_n, 'Loop'),
             (sum_prime_numbers_up_to_n_iter, 'Iter'),
             (sum_prime_numbers_up_to_n_high_order, 'High Order')]
    print('-- Running %d tests --' % number_of_tests)
    print('-- (Result for each is the total time spent per test) -- ')
    for (test_function, test_name) in tests:
        print('%s = %s ' % (test_name, str(timeit.timeit(test_function, number=number_of_tests))))

def sum_prime_numbers_up_to_n(n = DEFAULT_INPUT):
    if n < 2:
        return 0
    sum = 2
    if n > 2:
        i = 3
        while i < n:
            if is_prime(i):
                sum += i
            i += 2
    return sum

def sum_prime_numbers_up_to_n_iter(n = DEFAULT_INPUT):
    sum = 0
    for prime in iter(Prime()):
        if prime > n:
            break
        sum += prime
    return sum

# The time it takes to complete this is ludicrous compared
# to the other alternatives. Nevertheless, they have been
# left here for demonstration purposes.
def sum_prime_numbers_up_to_n_high_order(n = DEFAULT_INPUT):
    from functools import reduce
    primes = get_first_n_primes(n)
    return reduce(lambda x, y: x + y, primes)

def main():
    # Check for any command line argument
    if len(sys.argv) == 1:
        # No argument? Default it!
        result = sum_prime_numbers_up_to_n(DEFAULT_INPUT)
        print(result)
    else:
        # Even if there are more than one
        # arguments, we only care about the
        # first one, so let's continue.

        if sys.argv[1].isnumeric():
            result = sum_prime_numbers_up_to_n(int(sys.argv[1]))
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
