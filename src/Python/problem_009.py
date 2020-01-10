#!/usr/bin/env python3

# PROBLEM #9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:
#  a^2 + b^2 = c^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import sys
import timeit

DEFAULT_INPUT = 1000

def find_pythagorean_triplet(n = DEFAULT_INPUT):
    # Given the restriction: a < b < c,
    # we can rest assure that `c` needs to be at least half of N.
    # Following the same principle, for a < b, `a` cannot be
    # greater than a third of the total amount.
    for a in range(1, n//3 + 1):
        for b in range(a+1, n//2 + 1):
            # We can compute `c`, or its square, at least.
            c_sq = a * a + b * b
            # From a + b + c = N, we get that c = N - (a + b)
            # However, the real `c` is guaranteed to be positive,
            # so let's ignore any scenario where it's not.
            if n > a + b:
                # We know how much is c^2 and calculating square roots
                # is a bit expensive. Instead, if we square both sides of
                # c = N - (a + b), we can quickly check if this `c` is valid.
                temp = n - a - b
                if temp * temp == c_sq:
                    # Now that we're sure that's our `c`, we can compute it
                    # cheaply from a + b + c = N.
                    return (a, b, n - a - b)
    return None

# Given a value N, computes the product a*b*c, where
# a < b < c and a^2 + b^2 = c^2.
# If there's no triplet for such N, this will return None.
def compute_triplet_product(n = DEFAULT_INPUT):
    triplet = find_pythagorean_triplet(n)
    return (triplet[0] * triplet[1] * triplet[2]) if not triplet is None else None

def main():
    result = compute_triplet_product(DEFAULT_INPUT)
    print(result)

if __name__ == '__main__':
    main()