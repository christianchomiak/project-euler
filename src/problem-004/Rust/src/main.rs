/* [PROBLEM #4]
 * A palindromic number reads the same both ways.
 * The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 * Find the largest palindrome made from the product of two 3-digit numbers. */

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solution() {
        assert_eq!(compute_largest_palindrome(2), 9009);
        assert_eq!(compute_largest_palindrome(3), 906609);
    }
}

fn is_palindrome(number : u32) -> bool {
    let number_of_digits : u32 = (number as f64).log10() as u32 + 1;
    return match number_of_digits {
        1 => true,
        _ => {
            // TODO
            // Alternate solution without strings:
            //  Check first and last values (using / and %)
            //  Remove them:
            //    * If any leading zeroes were removed, check that the
            //      appropriate amount of zeroes can still be found on the right side.
            //    * Otherwise, recursively check the middle part of the number.

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

fn compute_largest_palindrome(digits : u32) -> u32 {
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
                    if number > largest && is_palindrome(number) {
                        largest = number;
                    }
                }
            }
            return largest;
        }
    }
}

fn main() {
    let result = compute_largest_palindrome(3);
    println!("{}", result);
}
