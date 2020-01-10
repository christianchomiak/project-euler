#!/usr/bin/env python3

# PROBLEM #2
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10.001st prime number?

import sys
import timeit
from euler_common import Prime, get_first_n_primes, is_prime

DEFAULT_INPUT = 10001

def time_performance():
    number_of_tests = 100

    tests = [(find_nth_prime_number, "Loop"),
             (find_nth_prime_number_list, "List"),
             (find_nth_prime_number_iter, "Iterator")]

    print("-- Running %d tests --" % number_of_tests)
    print("-- (Result for each is the total time spent per test) -- ")
    for (test_function, test_name) in tests:
        print("%s = %s " % (test_name, str(timeit.timeit(test_function, number=number_of_tests))))

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
    result = find_nth_prime_number_list(DEFAULT_INPUT)
    print(result)

if __name__ == '__main__':
    main()