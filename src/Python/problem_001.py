#!/usr/bin/env python3

# PROBLEM #1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def test_solution():
    assert sum_all_multiples(10) == 23
    assert sum_all_multiples(1000) == 233168

def sum_all_multiples(limit):
    sum = 0
    for n in range(limit):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum

def main():
    limit = 1000
    result = sum_all_multiples(limit)
    print(result)

if __name__ == '__main__':
    main()
    test_solution()