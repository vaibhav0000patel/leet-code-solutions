class Solution(object):

    

    def threeSum(self, nums):
        listOfTriplets = []    
        nums.sort()
        print(nums)
        iindex = 0
        jindex = len(nums)-1
        while iindex<jindex:
            invert = -(nums[iindex]+nums[jindex])
            if invert in nums[iindex+1:jindex]:
                triplet = [nums[iindex],invert,nums[jindex]]
                if triplet not in listOfTriplets:
                    listOfTriplets.append(triplet)
            if nums[jindex]<invert:
                iindex+=1
            else:
                jindex-=1
        return listOfTriplets

print ("Solution\""+str(Solution().threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))+"\"")

# [-1,0,1,2,-1,-4,-2,-3,3,0,4]
# [-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4]
# Output
# [[-4,0,4],[-4,1,3],[-3,0,3],[-3,1,2],[-2,0,2],[-1,0,1]]
# Expected
# [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
# [[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]

# [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]