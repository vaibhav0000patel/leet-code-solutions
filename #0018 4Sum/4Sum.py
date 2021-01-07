class Solution:
    def fourSum(self, nums, target):
        list_of_triplets = []
        nums.sort()
        for index,value in enumerate(nums):
            if index>0 and value==nums[index-1]:
                continue
            left_pointer = index+1
            right_pointer = len(nums)-1
            while left_pointer < right_pointer:
                three_sum = nums[left_pointer]+nums[index]+nums[right_pointer]
                if three_sum<target:
                    left_pointer+=1
                elif three_sum>target:
                    right_pointer-=1
                else:
                    list_of_triplets.append([nums[left_pointer],nums[index],nums[right_pointer]])
                    left_pointer+=1
                    while nums[left_pointer]==nums[left_pointer-1] and left_pointer<right_pointer:
                        left_pointer+=1
        return list_of_triplets

print ("Solution\""+str(Solution().fourSum([1,0,-1,0,-2,2],0))+"\"")