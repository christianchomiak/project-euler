/* [PROBLEM #3]
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143? */

 #[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solution() {
        assert_eq!(largest_prime_factor(13195), 29);
        assert_eq!(largest_prime_factor(600_851_475_143), 6_857);
        assert_eq!(is_prime(2), true);
        assert_eq!(is_prime(3), true);
        assert_eq!(is_prime(8), false);
        assert_eq!(is_prime(9), false);
        assert_eq!(is_prime(11), true);
        assert_eq!(is_prime(19), true);
        assert_eq!(is_prime(21), false);
        assert_eq!(is_prime(49), false);
        assert_eq!(is_prime(83), true);
        assert_eq!(is_prime(600_851_475_143), false);
    }
}

/// Returns whether the given `input` is a prime number or not.
/// This is based on the principle of Trial Division: https://en.wikipedia.org/wiki/Trial_division
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

fn largest_prime_factor(num : u64) -> u64 {
    if is_prime(num) {
        return num;
    }

    let mut vec : Vec<u64> = Vec::new();
    let mut i = 5;

    // For any N, all divisors of N are less than sqrt(N).
    // See: https://en.wikipedia.org/wiki/Primality_test
    while i * i <= num {
        if num % i == 0 && is_prime(i) {
            vec.push(i);
        }
        i += 2;
    }

    return match vec.last() {
        None => 1,
        Some(last) => *last
    }
}

fn main() {
    let result = largest_prime_factor(600_851_475_143);
    println!("{}", result);
}
