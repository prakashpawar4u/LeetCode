from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the input array to facilitate skipping duplicates and two-pointer technique
        nums.sort()
        result = []
        n = len(nums)

        # First loop: Fix the first number
        for i in range(n - 3):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Second loop: Fix the second number
            for j in range(i + 1, n - 2):
                # Skip duplicate values for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Use two pointers to find the remaining two numbers
                left, right = j + 1, n - 1

                while left < right:
                    # Calculate the sum of the four numbers
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total < target:
                        # Move the left pointer to the right to increase the sum
                        left += 1
                    elif total > target:
                        # Move the right pointer to the left to decrease the sum
                        right -= 1
                    else:
                        # Found a valid quadruplet
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates for the third number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        # Skip duplicates for the fourth number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # Move both pointers to look for the next pair
                        left += 1
                        right -= 1

        return result
