class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            if n in hashMap:
                return (hashMap[n], i)
            hashMap[target -n ] = i
        