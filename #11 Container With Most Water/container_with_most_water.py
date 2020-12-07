class Solution(object):
    
    def calculateArea(self,iindex,jindex,height):
        return (jindex-iindex)*min(height[iindex],height[jindex])

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        iindex = 0
        jindex = len(height)-1
        while(iindex<jindex):
            max_area = max(max_area,self.calculateArea(iindex,jindex,height))
            if height[iindex]<height[jindex]:
                iindex+=1
            else:
                jindex-=1
        return max_area

print ("Solution\""+str(Solution().maxArea([10,14,10,4,10,2,6,1,6,12]))+"\"")