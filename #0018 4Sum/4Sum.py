class Solution:
    def fourSum(self, nums, target):
        if not nums or len(nums)<4:
            return []
        fourSumList = []
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for l in range(k+1,len(nums)):
                        sumList = [nums[i],nums[j],nums[k],nums[l]]
                        sumList.sort()
                        if sum(sumList)==target and sumList not in fourSumList:
                            fourSumList.append(sumList)
        return fourSumList

print ("Solution\""+str(Solution().fourSum([1,0,-1,0,-2,2],0))+"\"")