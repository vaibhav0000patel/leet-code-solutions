class Solution(object):

    NUM_LIST = [
        (1000,"M"),
        (900,"CM"),
        (500,"D"),
        (400,"CD"),
        (100,"C"),
        (90,"XC"),
        (50,"L"),
        (40,"XL"),
        (10,"X"),
        (9,"IX"),
        (5,"V"),
        (4,"IV"),
        (1,"I")
    ]

    def intToRoman(self, num):
        roman = ""
        for numMap in self.NUM_LIST:
            if numMap[0]<=num:
                roman += numMap[1]*(num//numMap[0])
                num %= numMap[0]
            if not num:
                break
        return roman
    
print ("Solution\""+str(Solution().intToRoman(4))+"\"")
            
            
        