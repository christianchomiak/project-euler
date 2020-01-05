/* [PROBLEM #1]
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
 * The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000. */

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solution() {
        assert_eq!(sum_all_multiples(10), 23);
        assert_eq!(sum_all_multiples(1000), 233168);
    }
}

pub fn sum_all_multiples(limit: i32) -> i32 {
    let mut sum: i32 = 0;
    for n in 1..limit {
        if (n % 3 == 0) || (n % 5 == 0) {
            sum += n;
        }
    }
    return sum;
}

fn main() {
    let limit : i32 = 1000;
    let result : i32 = sum_all_multiples(limit);
    println!("{}", result);
}
