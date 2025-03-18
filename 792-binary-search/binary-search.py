class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Bruteforce
        # for i in range(len(nums)):
        #     if target==nums[i]:
        #         return i

        # return -1
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid -1
            else:
                low = mid +1
        return -1

                