class Solution:
    def nextGreaterElement(self, n: int) -> int:

        digits = list(str(n))
        i = len(digits) - 2

        # Step 1: Find first decreasing element from the right
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        if i == -1:
            return -1

        # Step 2: Find the next bigger digit to the right of i
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1

        # Step 3: Swap
        digits[i], digits[j] = digits[j], digits[i]

        # Step 4: Reverse the digits after position i
        digits[i + 1:] = reversed(digits[i + 1:])

        result = int(''.join(digits))

        # Step 5: Check if within 32-bit signed integer
        return result if result < (2 ** 31) else -1

            

        