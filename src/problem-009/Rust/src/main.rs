/* [PROBLEM #9]
 *
 * A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:
 *  a^2 + b^2 = c^2
 * There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 * 
 * Find the product abc. */

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_pythagorean_finder() {
        assert_ne!(find_pythagorean_triplet(1000), None);
    }

    #[test]
    fn test_triplet_product() {
        assert_eq!(compute_triplet_product(1000), Some(31875000));
    }

    #[test]
    fn test_pythagorean_checker() {
        assert_eq!(is_valid_pythagorean_triplet((1, 2, 3)), false);
        assert_eq!(is_valid_pythagorean_triplet((3, 4, 5)), true);
    }
}

#[allow(dead_code)]
fn is_valid_pythagorean_triplet((a, b, c) : (u32, u32, u32)) -> bool {
    a < b && b < c && (a*a + b*b == c*c)
}

// TODO: The current solution uses brute force to calculate (a, b, c).
//       Find a way to deduce the triplet in a better way.

/// Given a value N, finds the triplet (a,b,c), where
/// a < b < c and a^2 + b^2 = c^2.
/// If there's no triplet for such N, this will return None.
fn find_pythagorean_triplet(n : u32) -> Option<(u32, u32, u32)> {
    // Given the restriction: a < b < c,
    // we can rest assure that `c` needs to be at least
    // half of N.
    // Following the same principle, for a < b, `a` cannot be
    // greater than a third of the total amount.
    for a in 1..=n/3 {
        for b in a+1..=n/2 {
            // We can compute `c`, or its square, at least.
            let c_sq = a * a + b * b;
            // From a + b + c = N, we get that c = N - (a + b)
            // However, the real `c` is guaranteed to be positive,
            // so let's ignore any scenario where it's not.
            if n > a + b {
                // We know how much is c^2 and calculating square roots
                // is a bit expensive. Instead, if we square both sides of
                // c = N - (a + b), we can quickly check if this `c` is valid.
                let temp = n - a - b;
                if temp * temp == c_sq {
                    // Now that we're sure that's our `c`, we can compute it
                    // cheaply from a + b + c = N.
                    return Some((a, b, n - a - b));
                }
            }
        }
    }
    return None;
}

/// Given a value N, computes the product a*b*c, where
/// a < b < c and a^2 + b^2 = c^2.
/// If there's no triplet for such N, this will return None.
fn compute_triplet_product(n : u32) -> Option<u32> {
    let (a, b, c) = find_pythagorean_triplet(n)?;
    return Some(a * b * c);
}

fn main() {
    let n = 1000;
    match compute_triplet_product(n) {
        Some(result) => println!("{}", result),
        None => println!("There's no valid pythagorean triple for N = {}", n)
    }
}