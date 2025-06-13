class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            n = len(row)
            for i in range((n + 1) // 2):
                # Swap and invert in one step
                row[i], row[n - 1 - i] = 1 - row[n - 1 - i], 1 - row[i]
        return image