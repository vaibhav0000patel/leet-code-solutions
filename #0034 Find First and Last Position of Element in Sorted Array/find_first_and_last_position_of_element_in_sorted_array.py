from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1
        mid = (high+low)//2
        target_range = [-1,-1]
        if not nums or target>nums[high] or target<nums[low]:
            return target_range
        while nums[mid]!=target and high>low:
            if nums[mid]<target:
                low = mid+1
            else:
                high = mid-1
            mid = (high+low)//2
        low,high = mid,mid
        while low>=0 and nums[low]==target:
            target_range[0] = low
            low -= 1
        while high<len(nums) and nums[high]==target:
            target_range[1] = high
            high += 1
        return target_range


print ("Solution\""+str(Solution().searchRange([1],1))+"\"")