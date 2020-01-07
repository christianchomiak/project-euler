/* [PROBLEM #6]
 *
 * The sum of the squares of the first ten natural numbers is,
 *  1^2 + 2^2 + ... + 10^2 = 385
 * The square of the sum of the first ten natural numbers is,
 *  (1 + 2 + ... + 10)^2 = 55^2 = 3025
 * Hence, the difference between the sum of the squares of the
 * first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
 * 
 * Find the difference between the sum of the squares of the first
 * one hundred natural numbers and the square of the sum. */

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solution() {
        assert_eq!(compute_diff(10), 2640);
        assert_eq!(compute_diff(100), 25164150);
    }
}

fn compute_sum_of_squares(n : u32) -> u32 {
    return (n * (n + 1) * (2 * n + 1)) / 6;
}

fn compute_square_of_sum(n : u32) -> u32 {
    let sum = (n * (n + 1)) / 2;
    return sum * sum;
}

fn compute_diff(ceiling : u32) -> u32 {
    let sum_of_squares = compute_sum_of_squares(ceiling);
    let square_of_sum = compute_square_of_sum(ceiling);
    return square_of_sum - sum_of_squares;
}

fn main() {
    const CEILING : u32 = 100;
    let result = compute_diff(CEILING);
    println!("{}", result);
}