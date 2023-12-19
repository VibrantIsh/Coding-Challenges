# https://leetcode.com/problems/ugly-number/
impl Solution {
    pub fn is_ugly(mut n: i32) -> bool {
        if n < 1 {
            return false;
        }
        for prime in [2, 3, 5].iter() {
            while n % prime == 0 {
                n /= prime;
            }
        }
        n == 1
    }
}
