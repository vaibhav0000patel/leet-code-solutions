from typing import List

class Solution(object):
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = None
        closest_diff = None
        for index,value in enumerate(nums[:-2]):
            left_pointer = index+1
            right_pointer = len(nums)-1        
            while left_pointer < right_pointer:
                three_sum = nums[left_pointer]+nums[index]+nums[right_pointer]
                if three_sum<target:
                    left_pointer+=1
                elif three_sum>target:
                    right_pointer-=1
                else:
                    left_pointer+=1
                    right_pointer-=1
                diff = abs(target-three_sum)
                if closest_diff is None or diff<closest_diff:
                    closest_diff = diff
                    closest_sum = three_sum
        return closest_sum

print ("Solution\""+str(Solution().threeSumClosest([1,1,-1,-1,3],1))+"\"")