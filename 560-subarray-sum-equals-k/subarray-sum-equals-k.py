class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1  # Base case: one subarray with sum 0 before starting

        for num in nums:
            prefix_sum += num

            # Check if there's a previous prefix_sum that leads to current sum == k
            if (prefix_sum - k) in prefix_map:
                count += prefix_map[prefix_sum - k]

            # Record the current prefix sum
            prefix_map[prefix_sum] += 1

        return count