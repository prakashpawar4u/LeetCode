class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 2
        
        # Step 2: Find first decreasing digit from the right
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        
        if i == -1:
            return -1  # Already the highest permutation

        # Step 4: Find the next greater digit to swap with
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1
        
        # Step 5: Swap
        digits[i], digits[j] = digits[j], digits[i]
        
        # Step 6: Reverse the digits after the swapped position
        digits[i + 1:] = reversed(digits[i + 1:])
        
        result = int(''.join(digits))
        
        # Step 7: Check 32-bit integer constraint
        return result if result < 2**31 else -1
            