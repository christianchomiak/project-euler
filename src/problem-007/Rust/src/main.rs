/* [PROBLEM #7]
 *
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 * 
 * What is the 10.001st prime number? */

use std::time::{Instant};

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solution() {
        assert_eq!(find_nth_prime(6), 13);
        assert_eq!(find_nth_prime(10001), 104743);
        assert_eq!(find_nth_prime(10001), find_nth_prime_with_caching(10001));
    }
}

/// Returns true if `input` is only divisible by 1 and itself.
fn is_prime(input : u32) -> bool {
    match input {
        0 | 1 => return false,
        2 | 3 => return true,
        n => {
            if n % 2 == 0 || n % 3 == 0 {
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
                // We already have an odd number and we know that any even
                // number at this point will never be prime, so we can just
                // skip towards the next odd number.
                m += 2;
            }

            return true;
        }
    }
}

fn find_nth_prime_with_caching(n : u32) -> u32 {
    match n {
        0 | 1 => return 2,
        2 => return 3,
        _ => {
            // Even if we reserve enough space in memory in advance (e.g. vec![0; 100_000])
            // the performance seems to be worse than letting the vector grow organically.
            // This is particularily true when this function is called repeatedly.
            let mut primes : Vec<u32> = vec![2, 3];

            let mut current_number = 3;
            let mut i = 2;
            while i < n {
                // We already have an odd number and we know that any even
                // number at this point will never be prime, so we can just
                // skip towards the next odd number.
                current_number += 2;
                let mut is_prime = true;
                for i in 0..primes.len() {
                    if current_number % primes[i] == 0 {
                        is_prime = false;
                        break;
                    }
                }
                if is_prime {
                    primes.push(current_number);
                    i += 1;
                }
            }
            return *primes.last().unwrap();
        }
    }
}

fn find_nth_prime(n : u32) -> u32 {
    match n {
        0 | 1 => return 2,
        2 => return 3,
        _ => {
            let mut current_number = 3;
            let mut latest_prime = current_number;

            // How many primes have we found so far.
            let mut i = 2;

            while i < n {
                // We already have an odd number and we know that any even
                // number at this point will never be prime, so we can just
                // skip towards the next odd number.
                current_number += 2;
                if is_prime(current_number) {
                    latest_prime = current_number;
                    i += 1;
                }
            }
            return latest_prime;
        }
    }
}

#[allow(dead_code)]
fn compare_performance(number_of_test : usize) {
    let mut results = vec![(0, 0); number_of_test];
    let mut times_normal_was_better = 0;
    let mut times_alt_was_better = 0;

    const PRIME_TO_GET : u32 = 10001;

    for i in 0usize..number_of_test {
        let mut now = Instant::now();
        find_nth_prime(PRIME_TO_GET);
        let duration_normal = now.elapsed().as_micros();
    
        now = Instant::now();
        find_nth_prime_with_caching(PRIME_TO_GET);
        let duration_alt = now.elapsed().as_micros();

        results[i] = (duration_normal, duration_alt);

        if duration_normal > duration_alt {
            times_alt_was_better += 1;
        }
        else if duration_normal < duration_alt {
            times_normal_was_better += 1;
        }
        else {
            times_normal_was_better += 1;
            times_alt_was_better += 1;
        }
    }

    let mut avg_normal = 0f64;
    let mut avg_alt = 0f64;
    for i in 0usize..number_of_test {
        avg_normal += results[i].0 as f64;
        avg_alt += results[i].1 as f64;
    }
    avg_normal /= number_of_test as f64;
    avg_alt /= number_of_test as f64;
    let times_count = 100.0 / (times_normal_was_better + times_alt_was_better) as f64;

    println!("Avg. Normal: {}, Avg. Alt: {}", avg_normal, avg_alt);
    println!("Normal was better {}% of the times, Alt. was better {}% of the times",
            times_normal_was_better as f64 * times_count, times_alt_was_better as f64 * times_count);
}

fn main() {
    let result = find_nth_prime(10001);
    println!("{}", result);
    // compare_performance(10);
}