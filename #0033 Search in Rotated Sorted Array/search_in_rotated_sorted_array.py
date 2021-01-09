from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (high+low)//2
            if target==nums[mid]:
                return mid
            if nums[low]<=nums[mid]:
                if target>nums[mid] or target<nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if target<nums[mid] or target>nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1

print ("Solution\""+str(Solution().search([4,5,6,7,0,1,2],0))+"\"")
        