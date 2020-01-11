/* PROBLEM #8
 * The four adjacent digits in the 1000-digit number (see data.txt) that have the greatest product are:
 *  9 × 9 × 8 × 9 = 5832
 * Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
 * What is the value of this product?
 */

use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

const DATA_ROOT : &str = "../../../data/";
const DEFAULT_INPUT_DATA_FILENAME : &str = "problem_008.txt";
const DEFAULT_INPUT_DIGITS : u32 = 13;

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solution() {
        assert_eq!(load_data(DEFAULT_INPUT_DATA_FILENAME).len(), 1000);
        assert_eq!(find_greatest_product(4), 5832);
        assert_eq!(find_greatest_product(DEFAULT_INPUT_DIGITS), 23514624000);
    }
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filepath: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filepath)?;
    Ok(io::BufReader::new(file).lines())
}

fn load_data(filename : &str) -> Vec<u32> {
    let mut digits : Vec<u32> = Vec::new();

    let data_root = Path::new(DATA_ROOT);
    if !data_root.exists() {
        panic!("Could not find required data folder {:?}", data_root.canonicalize());
    }
    let data_root = match data_root.canonicalize() {
        Err(why) => panic!("{}", why),
        Ok(canonical_path) => canonical_path
    };

    let data_path = data_root.join(filename);
    if !data_path.exists() {
        panic!("Could not find required data file {:?} in path {}",
                filename, data_root.canonicalize().unwrap().display());
    }

    match read_lines(data_path) {
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
    return digits;
}

fn calculate_greatest_product(adjacent_digits : u32, digits : &Vec<u32>) -> u64 {
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

fn find_greatest_product(adjacent_digits : u32) -> u64 {
    let digits = load_data(DEFAULT_INPUT_DATA_FILENAME);
    return calculate_greatest_product(adjacent_digits, &digits);
}

fn main() {
    let result = find_greatest_product(DEFAULT_INPUT_DIGITS);
    println!("{}", result);
}