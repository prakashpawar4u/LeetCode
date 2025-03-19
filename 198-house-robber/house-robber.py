class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        if n == 1:
            return nums[0]
        
        prev = 0 
        curr = nums[0]

        for i in range(2, n + 1):
            new_curr = max(curr, prev + nums[i -1])
            prev = curr
            curr = new_curr
        return curr
        