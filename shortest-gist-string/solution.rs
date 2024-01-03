use std::collections::HashMap;
use std::collections::HashSet;

fn slide_smallest(word: String) -> usize {
    if word.len() <= 1 {
        return word.len();
    }

    let mut prefix_hash: HashMap<char, i32> = HashMap::new();
    let mut curr_begin: usize = 0;
    let mut best_begin: usize = 0;
    let mut distinct_cnt: i32 = 1;
    let mut best_len: usize = word.len();
    let mut curr_len: usize = word.len();

    let letter_hash: HashSet<char> = word.chars().collect();

    if let Some(first_char) = word.chars().next() {
        prefix_hash.insert(first_char, 1);
    }

    for (index, c) in word.chars().skip(1).enumerate() {
        if let Some(count) = prefix_hash.get_mut(&c) {
            *count += 1;
        } else {
            prefix_hash.insert(c, 1);
            distinct_cnt += 1;
        }

        if distinct_cnt as usize == letter_hash.len() {
            // Remove unnecessary prefix
            while prefix_hash[&word.chars().nth(curr_begin).unwrap()] > 1 {
                if let Some(count) = prefix_hash.get_mut(&word.chars().nth(curr_begin).unwrap()) {
                    *count -= 1;
                }
                curr_begin += 1;
            }
            curr_len = index + 1 - curr_begin + 1; // +1 because of skipping
            if curr_len < best_len {
                best_len = curr_len;
                best_begin = curr_begin;
            }
        }
    }

    best_len
}

fn main() {
    let str = String::from("juijutsu");
    println!("{}", slide_smallest(str));

    let str1 = String::from("aabcbcdbca");
    println!("{}", slide_smallest(str1));
}
