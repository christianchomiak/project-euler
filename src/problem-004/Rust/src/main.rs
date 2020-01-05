/* [PROBLEM #4]
 * A palindromic number reads the same both ways.
 * The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 * Find the largest palindrome made from the product of two 3-digit numbers. */

 use std::time::{Instant};

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solution() {
        assert_eq!(compute_largest_palindrome(2, is_palindrome_no_strings_no_recursions), 9009);
        assert_eq!(compute_largest_palindrome(3, is_palindrome_no_strings_no_recursions), 906609);
    }
    #[test]
    fn test_checkers() {
        test_checker(is_palindrome_string_check);
        test_checker(is_palindrome_no_strings);
        test_checker(is_palindrome_no_strings_no_recursions);
    }

    fn test_checker(is_palindrome_fn: fn(u32) -> bool) {
        assert_eq!(is_palindrome_fn(0), true);
        assert_eq!(is_palindrome_fn(1), true);
        assert_eq!(is_palindrome_fn(11), true);
        assert_eq!(is_palindrome_fn(101), true);
        assert_eq!(is_palindrome_fn(1001), true);
        assert_eq!(is_palindrome_fn(10101), true);
        assert_eq!(is_palindrome_fn(90100109), true);
        assert_eq!(is_palindrome_fn(26541), false);
        assert_eq!(is_palindrome_fn(45), false);
        assert_eq!(is_palindrome_fn(456), false);
        assert_eq!(is_palindrome_fn(100000), false);
        assert_eq!(is_palindrome_fn(100001), true);
    }
}

/// Naive solution: Use strings to easily check if the digits match.
fn is_palindrome_string_check(number : u32) -> bool {
    let number_of_digits : u32 = (number as f64).log10() as u32 + 1;
    return match number_of_digits {
        1 => true,
        _ => {
            let as_string = number.to_string();
            let digits_array = as_string.as_bytes();
            let half = number_of_digits / 2;
            for i in 0..half {
                let first_index = (number_of_digits - i - 1) as usize;
                let second_index = i as usize;
                if digits_array[first_index] != digits_array[second_index] {
                    return false;
                }
            }
            return true;
        }
    }
}

/// A better solution to is_palindrome_string_check() as it doesn't
/// require the expensive String type. Instead, it uses math(R)(tm)
/// to extract the digits out of the initial number.
fn is_palindrome_no_strings(number : u32) -> bool {
    let number_of_digits : i32 = if number != 0 { (number as f64).log10() as i32 + 1 } else { 1 };
    return match number_of_digits {
        1 => true,
        _ => {
            let closest = 10u32.pow(number_of_digits as u32 - 1);
            let first = number / closest;
            let last = number % 10;

            let expected_digits_after : i32 = number_of_digits - 2;
            let mut middle = (number - (first * closest) - last) / 10;
            let actual_digits_after : i32 = (middle as f64).log10() as i32 + 1;

            // No need to continue if we already know the number cannot be a palindrome.
            if first != last {
                return false;
            }

            // Is it worthy to continue checking the middle?
            if middle != 0 {
                // After removing the leading digit, we may have 1 or more zeroes.
                // Because leading zeroes are ignored, the middle value will be malformed
                // for furture checks.
                // e.g. After removing the edge 1s, 10101 becomes 10 instead of 010.
                // Knowing this, if there's a mismatch in the number of digits, we expected
                // the middle portion to have the same amount of trailing zeroes.
                if expected_digits_after > 0 && actual_digits_after != expected_digits_after {
                    let number_of_zeroes = expected_digits_after - actual_digits_after;
                    for _ in 1..=number_of_zeroes {
                        if middle % 10 != 0 {
                            return false;
                        }
                        // Shorten the middle by discarding its trail.
                        middle /= 10;
                    }
                }
            }

            return is_palindrome_no_strings(middle);
        }
    }
}

/// An even better solution than is_palindrome_no_strings().
/// This avoids Strings and recursions altogether. The result
/// is a further improvement in the overall performance.
/// See: measure_performance_no_strings()
fn is_palindrome_no_strings_no_recursions(number : u32) -> bool {
    let mut middle = number;
    let mut number_of_digits : i32 = if middle != 0 { (middle as f64).log10() as i32 + 1 } else { 1 };
    loop {
        match number_of_digits {
            0 => return true,
            1 => return true,
            _ => {
                let closest = 10u32.pow(number_of_digits as u32 - 1);
                let first = middle / closest;
                let last = middle % 10;

                // No need to continue if we already know the number cannot be a palindrome.
                if first != last {
                    return false;
                }

                // Find the new remainder
                middle = (middle - (first * closest) - last) / 10;

                // Discount the edges
                number_of_digits -= 2;

                // Is it worthy to continue checking the middle?
                if middle != 0 {
                    let actual_digits : i32 = (middle as f64).log10() as i32 + 1;

                    // After removing the leading digit, we may have 1 or more zeroes.
                    // Because leading zeroes are ignored, the middle value will be malformed
                    // for furture checks.
                    // e.g. After removing the edge 1s, 10101 becomes 10 instead of 010.
                    // Knowing this, if there's a mismatch in the number of digits, we expected
                    // the middle portion to have the same amount of trailing zeroes.
                    if number_of_digits > 0 && actual_digits != number_of_digits {
                        let number_of_zeroes = number_of_digits - actual_digits;
                        for _ in 1..=number_of_zeroes {
                            if middle % 10 != 0 {
                                return false;
                            }
                            // Shorten the middle by discarding its trail.
                            middle /= 10;
                        }
                        // Zeroes are removed twice because they were both leading and trailing.
                        number_of_digits -= 2 * number_of_zeroes;
                    }
                }
            }
        }
    }
}

fn compute_largest_palindrome(digits : u32, is_palindrome_fn: fn(u32) -> bool) -> u32 {
    match digits {
        0 => panic!("All numbers need to have at least one digit"),
        _ => {
            let mut largest = 0;

            // e.g. For 2-digit numbers, we only need to check
            //      values between 10 and 99.
            let floor = 10u32.pow(digits - 1);
            let ceiling = 10u32.pow(digits);

            for i in floor..ceiling {
                for j in floor..ceiling {
                    let number = i * j;
                    if number > largest && is_palindrome_fn(number) {
                        largest = number;
                    }
                }
            }
            return largest;
        }
    }
}

// For a 10.000 tests in a release build:
// The non-recursive solution was 94.9% of the times quicker.
#[allow(dead_code)]
fn measure_performance_no_strings(number_of_test : usize) {
    let mut results = vec![(0, 0); number_of_test];
    let mut times_recursive_was_better = 0;
    let mut times_non_recursive_was_better = 0;

    for i in 0usize..number_of_test {
        let mut now = Instant::now();
        compute_largest_palindrome(3, is_palindrome_no_strings);
        let duration_recursive = now.elapsed().as_micros();
    
        now = Instant::now();
        compute_largest_palindrome(3, is_palindrome_no_strings_no_recursions);
        let duration_non_recursive = now.elapsed().as_micros();

        results[i] = (duration_recursive, duration_non_recursive);

        if duration_recursive > duration_non_recursive {
            times_non_recursive_was_better += 1;
        }
        else if duration_recursive < duration_non_recursive {
            times_recursive_was_better += 1;
        }
    }

    let mut avg_recursive = 0f64;
    let mut avg_non_recursive = 0f64;
    for i in 0usize..number_of_test {
        avg_recursive += results[i].0 as f64;
        avg_non_recursive += results[i].1 as f64;
    }
    avg_recursive /= number_of_test as f64;
    avg_non_recursive /= number_of_test as f64;
    let times_count = 100.0 / (times_recursive_was_better + times_non_recursive_was_better) as f64;

    println!("Avg. Recursive: {}, Avg. Non-recursive: {}", avg_recursive, avg_non_recursive);
    println!("Recursive was better {}% of the times, Non-recursive was better {}% of the times",
            times_recursive_was_better as f64 * times_count, times_non_recursive_was_better as f64 * times_count);

    /*println!("Recursive | Non-recursive");
    println!("-------------------------");
    for i in 0usize..number_of_test {
        println!("{}{}     | {}{}",
            results[i].0,
            if results[i].0 < results[i].1 {'*'} else {' '},
            results[i].1,
            if results[i].0 < results[i].1 {' '} else {'*'});
    }*/
}

#[allow(dead_code)]
fn measure_performance_3_solutions() {
    let mut now = Instant::now();
    let result1 = compute_largest_palindrome(3, is_palindrome_string_check);
    let duration1 = now.elapsed().as_micros();

    now = Instant::now();
    let result2 = compute_largest_palindrome(3, is_palindrome_no_strings);
    let duration2 = now.elapsed().as_micros();

    now = Instant::now();
    let result3 = compute_largest_palindrome(3, is_palindrome_no_strings_no_recursions);
    let duration3 = now.elapsed().as_micros();

    println!("{}", result2);
    assert_eq!(result1, result2, "is_palindrome_string_check() doesn't match is_palindrome_no_strings()");
    assert_eq!(result2, result3, "is_palindrome_no_strings() doesn't match is_palindrome_no_strings_no_recursions()");

    println!("[Performance test]");
    println!("1: is_palindrome_string_check:  {} micros", duration1);
    println!("2: is_palindrome_no_strings: {} micros", duration2);
    println!("3: is_palindrome_no_strings_no_recursions: {} micros", duration3);
    println!("------------------------");
    if duration1 > duration2 {
        println!("[2] was {} times faster than [1]!", duration1 as f32 / duration2 as f32);
    }
    else {
        println!("[1] was {} times faster than [2]!", duration2 as f32 / duration1 as f32);
    }
    if duration2 > duration3 {
        println!("[3] was {} times faster than [2]!", duration2 as f32 / duration3 as f32);
    }
    else {
        println!("[2] was {} times faster than [3]!", duration3 as f32 / duration2 as f32);
    }
}

fn main() {
    let result = compute_largest_palindrome(3, is_palindrome_no_strings_no_recursions);
    println!("{}", result);
}
