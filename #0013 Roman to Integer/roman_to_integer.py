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

    def romanToInt(self, s):
        digit = 0
        for numMap in self.NUM_LIST:
            while s.startswith(numMap[1]):
                digit += numMap[0]
                s = s[len(numMap[1]):]
            if not s:
                break
        return digit
    
print ("Solution\""+str(Solution().romanToInt("MCMXCIV"))+"\"")