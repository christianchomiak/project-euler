/* [PROBLEM #10]
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 * Find the sum of all the primes below two million. */

 #[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solution() {
        assert_eq!(sum_prime_numbers(10), 17);
        assert_eq!(sum_prime_numbers(2_000_000), 142913828922);
    }
}

/// Returns true if `input` is only divisible by 1 and itself.
fn is_prime(input : u64) -> bool {
    match input {
        0 | 1 => return false,
        2 | 3 => return true,
        n if n % 2 == 0 || n % 3 == 0 => return false,
        n => {
            let mut m = 5;

            // Any divisor will always be less than sqrt(N),
            // no need to check further than that.
            // See: https://en.wikipedia.org/wiki/Primality_test
            while m * m <= n {
                if n % m == 0 {
                    return false;
                }
                m += 2;
            }
            return true;
        }
    }
}

// TODO: Check if this can also be solved using an iterator to generate
//       the prime numbers.

/// Returns the sum of all the prime numbers below `ceiling`.
fn sum_prime_numbers(ceiling : u64) -> u64 {
    match ceiling {
        // There're no prime number below 2.
        0 | 1 => return 0,
        _ => {
            let mut sum = 0u64;
            for i in 2.. {
                if is_prime(i) {
                    sum += i;
                }
                if i >= ceiling {
                    break;
                }
            }
            return sum;
        }
    }
}

fn main() {
    const CEILING : u64 = 2_000_000;
    let result = sum_prime_numbers(CEILING);
    println!("{}", result);
}