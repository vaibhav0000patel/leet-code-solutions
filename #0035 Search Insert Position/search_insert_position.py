from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        mid = (high+low)//2
        if target>nums[high]:
            return high+1
        if target<nums[low]:
            return low
        while nums[mid]!=target and high>low:
            if nums[mid]<target:
                low = mid+1
            else:
                high = mid-1
            mid = (high+low)//2
        return mid if target<=nums[mid] else mid+1




print ("Solution\""+str(Solution().searchInsert([1,3,5,6],5))+"\"")
        