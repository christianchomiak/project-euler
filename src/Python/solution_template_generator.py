#!/usr/bin/env python3

import sys

if (sys.argv == 1):
    print("Missing problem number")
    sys.exit()

filename = sys.argv[1]

orig_stdout = sys.stdout
f = open("%s.py" % filename, 'w')
sys.stdout = f

print('#!/usr/bin/env python3')
print()
print('# PROBLEM -1 # TODO: Add problem number here')
print('# TODO: Add description here')
print()
print('import sys')
print('import timeit')
print()
print('DEFAULT_INPUT = 0 # TODO: Add value here')
print('DEFAULT_NUMBER_OF_TESTS = 10 # TODO: Add value here')
print()
print('def test_solution(input, expected_result):')
print('    result = SOLUTION(input)')
print('    assert result == expected_result, " Test FAILED, expected: " + str(expected_result) + ", got: " + str(result)')
print()
print('def test_solutions():')
print('    # test_solution(DEFAULT_INPUT, 0) # TODO: Add expected value here')
print('    print("All Tests OK")')
print()
print('def time_performance(number_of_tests = DEFAULT_NUMBER_OF_TESTS):')
print('    # TODO: Add proper test name here')
print('    tests = [(SOLUTION, "Test_Name")]')
print('    print("Testing %d solution(s), running %d tests for each one." % (len(tests), number_of_tests))')
print('    print("The result is the time spent per solution.")')
print('    for (test_function, test_name) in tests:')
print('        print("%s = %s " % (test_name, str(timeit.timeit(test_function, number=number_of_tests))))')
print()
print('# TODO: Rename this')
print('def SOLUTION(x = DEFAULT_INPUT):')
print('    return x')
print()
print('def main():')
print('    # Check for any command line argument')
print('    if len(sys.argv) == 1:')
print('        # No argument? Default it!')
print('        result = SOLUTION(DEFAULT_INPUT)')
print('        print(result)')
print('    else:')
print('        # Even if there are more than one')
print('        # arguments, we only care about the')
print('        # first one, so let\'s continue.')
print()
print('        if sys.argv[1].isnumeric():')
print('            result = SOLUTION(int(sys.argv[1]))')
print('            print(result)')
print('        elif sys.argv[1] == "--test":')
print('            test_solutions()')
print('        elif sys.argv[1] == "--time":')
print('            time_performance()')
print('        elif sys.argv[1] != "--help":')
print('                print("Unknown option %s" % sys.argv[1])')
print('                print("usage: %s {[arg]|option}" % sys.argv[0])')
print('                print("Try `%s --help` for more information." % sys.argv[0])')
print('        else:')
print('            print("Usage:")')
print('            print("     %s {[arg]|option}" % sys.argv[0])')
print('            print("Where:")')
print('            # TODO: Add argument description here')
print('            print("    arg: <Argument Description>.")')
print('            print("         Default: %d" % DEFAULT_INPUT)')
print('            print("    option:")')
print('            print("        --test  : Run the unit tests")')
print('            print("        --time  : Measure the performance of different solutions to the problem")')
print('            print("        --help  : Show this help")')
print('    return')
print()
print('if __name__ == "__main__":')
print('    main()')

sys.stdout = orig_stdout

f.close()

print("DONE")