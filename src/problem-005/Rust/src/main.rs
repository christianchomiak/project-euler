/* [PROBLEM #5]
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? */

 use std::time::{Duration, Instant};

 #[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solution() {
        assert_eq!(compute_smallest_evenly_divisible_number(10), 2520);
        assert_eq!(compute_smallest_evenly_divisible_number(20), 232792560);
    }
    #[test]
    fn test_values() {
        for i in 1..=4 {
            let result = compute_smallest_evenly_divisible_number(10 * i);
            assert_eq!(is_evenly_divisible_number(result, 10 * i), true);
        }
    }

    /// Returns true if `number` is evenly divisible (a % b == 0)
    /// by all numbers from 1 to ceiling, both included.
    fn is_evenly_divisible_number(number : u64, ceiling : u64) -> bool {
        for i in 2..=ceiling {
            if number % i != 0 {
                return false;
            }
        }
        return true;
    }
}

/// Returns true if `input` is only divisible by 1 and itself.
fn is_prime(input : u64) -> bool {
    match input {
        0 | 1 => return false,
        2 | 3 => return true,
        n => {
            if n % 2 == 0 || n % 3 == 0{
                return false;
            }

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

/// Returns all the prime numbers below or equal to `ceiling`.
fn generate_prime_numbers(ceiling : u64) -> Vec<u64> {
    let mut primes = vec![];
    for i in 2..=ceiling {
        if is_prime(i) {
            primes.push(i);
        }
    }
    return primes;
}

/// Returns the smallest number that is evenly divided by all
/// numbers from 1 up to `ceiling`.
/// A is evenly divided by B if A % B == 0.
fn compute_smallest_evenly_divisible_number(ceiling : u64) -> u64 {
    // To be fair, `ceiling` could be defined as an i8.
    // Trying to call this function with a value greater than 46
    // will result in an overflow by multiplication.
    // However, it was left as u64 as everything else in this function is u64.

    // All primes up to `ceiling`.
    let primes = generate_prime_numbers(ceiling);
    let mut result = 1u64;

    // We'll use the inverse of integer factorization
    // and try to construct our number out of the list
    // of primes we have available.
    for prime in primes {
        // We need to maximise the times this prime appears,
        // so we'll build the biggest composite number made
        // using that prime only.
        // However, this new number must abide by the rules
        // and still be no greater than `ceiling`.
        let mut powered_prime = prime;
        while powered_prime * prime <= ceiling {
            powered_prime *= prime;
        }
        result *= powered_prime;
    }

    return result;
}

// For a million runs, the average speed is about 700ns (give or take) in a release build.
#[allow(dead_code)]
fn measure_performance(number_of_test : i32) {
    let mut accumulated : Duration = Duration::new(0, 0);
    for _ in 0..number_of_test {
        let now = Instant::now();
        compute_smallest_evenly_divisible_number(40);
        let duration = now.elapsed();

        accumulated += duration;
    }
    let average = accumulated.div_f64(number_of_test as f64);

    println!("For a total of {} tests, the average speed was {:?}", number_of_test, average);
}

fn main() {
    const CEILING : u64 = 20;
    let result = compute_smallest_evenly_divisible_number(CEILING);
    println!("{}", result);
}