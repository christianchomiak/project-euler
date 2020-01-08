#!/usr/bin/env python3

# PROBLEM #1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import sys

def test_solution(input, expected_result):
    result = sum_all_multiples(input)
    assert result == expected_result, "Test FAILED, expected: " + str(expected_result) + ", got: " + str(result)

def test_solutions():
    test_solution(10, 23)
    test_solution(1000, 233168)
    print("Tests OK")

def sum_all_multiples(limit):
    sum = 0
    for n in range(limit):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum

def main():
    if len(sys.argv) - 1 == 0:
        # No argument? Default it!
        limit = 1000
    else:
        # Even if there are more than one
        # arguments, we only care about the
        # first one, so let's continue.

        if sys.argv[1].isnumeric():
            limit = int(sys.argv[1])
        elif sys.argv[1] == 'test':
            test_solutions()
            return
        else:
            sys.exit("Expected an integer")
    result = sum_all_multiples(limit)
    print(result)

if __name__ == '__main__':
    main()