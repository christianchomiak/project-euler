#!/usr/bin/env python3

# PROBLEM 8
# The four adjacent digits in the 1000-digit number (see data.txt) that have the greatest product are:
#   9 × 9 × 8 × 9 = 5832
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?

import sys
import timeit
from pathlib import Path

DATA_ROOT = "../../data/"
DEFAULT_INPUT_DATA = "problem_008.txt"
DEFAULT_INPUT_DIGITS = 13
DEFAULT_NUMBER_OF_TESTS = 1000

def test_solution(input, expected_result, data):
    result = find_greatest_product(data, input)
    assert result == expected_result, ' Test FAILED, expected: ' + str(expected_result) + ', got: ' + str(result)

def test_solutions():
    digits = load_digits_from_file(DEFAULT_INPUT_DATA)
    assert len(digits) == 1000, ' Test FAILED, data must contain 1000 numerical digits, instead of %d' % len(digits)

    test_solution(4, 5832, digits)
    test_solution(13, 23514624000, digits)
    print('All Tests OK')

def time_performance(number_of_tests = DEFAULT_NUMBER_OF_TESTS):
    # The solutions require data read from a file. This process
    # should only be executed once and the result passed directly
    # to the code we want to test, as we're interested in measuring
    # the performance of the product finder and not the data loading.
    digits = load_digits_from_file(DEFAULT_INPUT_DATA)

    tests = [(find_greatest_product, 'Naive')]

    print('Testing %d solution(s), running %d tests for each one.' % (len(tests), number_of_tests))
    print('The result is the time spent per solution.')
    for (test_function, test_name) in tests:
        test_length = timeit.timeit(lambda: test_function(digits), number=number_of_tests)
        print('    %s = %s ' % (test_name, str(test_length)))
    return

def load_digits_from_file(filename = DEFAULT_INPUT_DATA):
    digits = []

    data_path = Path(DATA_ROOT) / filename

    if not data_path.exists():
        print("Error: Couldn't find data file '%s'" % data_path.resolve())
        return []

    # The file will get automatically closed at the end
    # of the WITH statement.
    with open(data_path, 'r') as digits_file:
        for line in digits_file.readlines():
            # Separate line by characters
            for character in line:
                # Are the character actually numbers?
                if character.isnumeric():
                    digits.append(int(character))

    return digits

def find_greatest_product(list_of_digits, adjacent_digits = DEFAULT_INPUT_DIGITS):
    slize_size = min(adjacent_digits, len(list_of_digits))

    greatest_product = 1
    for i in range(len(list_of_digits) - slize_size):
        product = 1
        for j in range(slize_size):
            product *= list_of_digits[i + j]
        if product > greatest_product:
            greatest_product = product

    return greatest_product

def solution(digits_filename = DEFAULT_INPUT_DATA, adjacent_digits = DEFAULT_INPUT_DIGITS):
    digits = load_digits_from_file(digits_filename)
    return find_greatest_product(digits, adjacent_digits)

def main():
    amount_of_arguments = len(sys.argv) - 1
    # Check for any command line argument
    if amount_of_arguments == 0:
        # No argument? Default it!
        result = solution()
        print(result)
    else:
        # Even if there are more than two arguments,
        # we only care about the first two, so let's continue.
        if amount_of_arguments >= 2 and sys.argv[2].isnumeric():
            filename = sys.argv[1]
            digits = int(sys.argv[2])
            result = solution(filename, digits)
            print(result)
        elif sys.argv[1] == "--test":
            test_solutions()
        elif sys.argv[1] == "--time":
            time_performance()
        elif sys.argv[1] != "--help":
                from functools import reduce
                print("Unknown argument '%s'" % reduce(lambda x, y: x + ' ' + y, sys.argv[1:]))
                print("usage: %s {[arg1 arg2]|option}" % sys.argv[0])
                print("Try `%s --help` for more information." % sys.argv[0])
        else:
            print("Usage:")
            print("     %s {[arg1 arg2]|option}" % sys.argv[0])
            print("Where:")
            print("    arg1: Name of the file containing the data.")
            print("          Default: '%s'" % DEFAULT_INPUT_DATA)
            print("          Data must be placed in: '%s'" % Path(DATA_ROOT).resolve())
            print("    arg2: Amount of digits to check.")
            print("          Default: %d" % DEFAULT_INPUT_DIGITS)
            print("    option:")
            print("        --test  : Run the unit tests")
            print("        --time  : Measure the performance of different solutions to the problem")
            print("        --help  : Show this help")
    return

if __name__ == '__main__':
    main()
