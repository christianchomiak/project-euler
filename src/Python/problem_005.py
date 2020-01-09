#!/usr/bin/env python3

# PROBLEM #4
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

import timeit
from euler_common import Prime, is_prime

DEFAULT_INPUT = 20

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

def time_performance():
    number_of_tests = 1000000

    tests = [(compute_smallest_evenly_divisible_number, "Loop"),
             (compute_smallest_evenly_divisible_number_iterator, "Iterator")]

    print("-- Running %d tests --" % number_of_tests)
    print("-- (Result for each is the total time spent per test) -- ")
    for (test_function, test_name) in tests:
        print("%s = %s " % (test_name, str(timeit.timeit(test_function, number=number_of_tests))))

def main():
    result = compute_smallest_evenly_divisible_number(DEFAULT_INPUT)
    print(result)
    # time_performance()

if __name__ == '__main__':
    main()