// https://leetcode.com/problems/happy-number/
impl Solution {
    pub fn is_happy(n: i32) -> bool {
        fn get_next(mut n: i32) -> i32 {
            let mut sum = 0;
            while n > 0 {
                let digit = n % 10;
                sum += digit * digit;
                n /= 10;
            }
            sum
        }

        let mut slow = n;
        let mut fast = get_next(n);

        while fast != 1 && slow != fast {
            slow = get_next(slow);
            fast = get_next(get_next(fast));
        }

        fast == 1
    }
}
