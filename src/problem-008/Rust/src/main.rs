/* PROBLEM #8
 * The four adjacent digits in the 1000-digit number (see data.txt) that have the greatest product are:
 *  9 × 9 × 8 × 9 = 5832
 * Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
 */

use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solution() {
        assert_eq!(find_greatest_product(4), 5832);
        assert_eq!(find_greatest_product(13), 23514624000);
    }
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn find_greatest_product(adjacent_digits : u32) -> u64 {
    let mut digits : Vec<u32> = Vec::new();
    let filename = "data.txt";

    match read_lines(filename) {
        Ok(lines) => {
            for result_line in lines {
                match result_line {
                    Ok(line) => {
                        // Separate line by characters
                        for string in line.split("") {
                            // Are the character actually numbers?
                            if let Ok(number) = string.parse() {
                                digits.push(number);
                            }
                        }
                    },
                    Err(why) => panic!("{}", why)
                }
            }
        },
        Err(why) => panic!("{}", why)
    }

    let slize_size = std::cmp::min(adjacent_digits, digits.len() as u32) as usize;

    let mut greatest_product = 1u64;
    for i in 0..(digits.len() - slize_size) {
        let mut product = 1u64;
        for j in 0..slize_size {
            product *= digits[i + j] as u64;
        }
        if product > greatest_product {
            greatest_product = product;
        }
    }
    return greatest_product;
}

fn main() {
    let result = find_greatest_product(13);
    println!("{}", result);
}