from typing import List

class Solution:

    def reverse(self,nums:List[int],i:int) -> None:
        j = len(nums)-1
        while(i<j):
            self.swap(nums,i,j)
            i+=1
            j-=1
    
    def swap(self,nums:List[int],i:int,j:int) -> None:
        nums[i],nums[j] = nums[j],nums[i]

    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-2
        while(i>=0 and nums[i+1]<=nums[i]):
            i-=1
        if (i>=0):
            j = len(nums)-1
            while(j>=0 and nums[j]<=nums[i]):
                j-=1
            self.swap(nums,i,j)
        self.reverse(nums,i+1)

list_a = [5,1,1]
Solution().nextPermutation(list_a)
print ("Solution\""+str(list_a)+"\"")

# Output [1,5,1]
# Expected [1,1,5]