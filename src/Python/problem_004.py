#!/usr/bin/env python3

# PROBLEM #4
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from euler_common import is_palindrome

def compute_largest_palindrome(number_of_digits):
    if number_of_digits < 1:
        return None

    largest = 0
    floor = 10**(number_of_digits - 1)
    ceiling = 10**number_of_digits

    for i in range(floor, ceiling):
        for j in range(floor, ceiling):
            product = i * j
            if product > largest and is_palindrome(str(product)):
                largest = product

    return largest

DEFAULT_INPUT = 3

def main():
    result = compute_largest_palindrome(DEFAULT_INPUT)
    print(result)

if __name__ == '__main__':
    main()