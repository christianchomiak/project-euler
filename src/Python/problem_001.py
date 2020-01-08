#!/usr/bin/env python3

# PROBLEM #1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import sys

def test_solution(input, expected_result):
    result = sum_all_multiples(input)
    assert result == expected_result, "Test FAILED, expected: " + str(expected_result) + ", got: " + str(result)
    print("Test Ok, sum_all_multiples(%s) == %s" % (input, expected_result))

def test_solutions():
    test_solution(10, 23)
    test_solution(1000, 233168)
    print("All Tests OK")

def sum_all_multiples(ceiling):
    sum = 0
    for n in range(ceiling):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum

def main():
    default_input = 1000

    # Check for any command line argument
    if len(sys.argv) - 1 == 0:
        # No argument? Default it!
        ceiling = default_input
    else:
        # Even if there are more than one
        # arguments, we only care about the
        # first one, so let's continue.

        if sys.argv[1].isnumeric():
            ceiling = int(sys.argv[1])
        elif sys.argv[1] == '--test':
            test_solutions()
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
            print("    arg: The ceiling used by the algorithm. Default: %d" % default_input)
            print("    option:")
            print("        --test  : Run the unit tests")
            print("        --help  : Show this help")
            return

    result = sum_all_multiples(ceiling)
    print(result)

if __name__ == '__main__':
    main()