class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter_st = [c.lower() for c in s if c.isalnum()]
        return filter_st == filter_st[::-1]

        