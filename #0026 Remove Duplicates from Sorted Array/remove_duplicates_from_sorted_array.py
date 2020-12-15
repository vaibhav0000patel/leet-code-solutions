class Solution:
    def removeDuplicates(self, nums):
        index = 0
        lastNum = None
        while index<len(nums):
            if lastNum is None or nums[index]!=lastNum:
                lastNum = nums[index]
                index+=1
                continue
            nums.pop(index)
        return len(nums)



print ("Solution\""+str(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))+"\"")