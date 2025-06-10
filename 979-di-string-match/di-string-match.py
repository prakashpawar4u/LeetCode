class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        result = []
        for ch in s:
            if ch == 'I':
                result.append(low)
                low += 1
            else:  # ch == 'D'
                result.append(high)
                high -= 1

        result.append(low)  # or high, both are same at this point
        return result
        