class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        history = {}
        for index,number in enumerate(nums):
            leftover = target-number
            if leftover in history:
                return [history[leftover],index]
            history[number] = index
        return []