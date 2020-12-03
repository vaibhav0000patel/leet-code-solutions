import math
class Solution(object):
    def myAtoi(self, s):
        index = 0
        filteredString = ""
        s = s.strip()
        s_len = len(s)
        while index<s_len and s[index] in ["-","+"]:
            filteredString += s[index] if s[index] in ["-"] else ""
            index+=1
            break
        while index<s_len and s[index].isnumeric():
            filteredString += s[index]
            index+=1
        number = 0
        if filteredString and (len(filteredString)>1 or filteredString[0] not in ["-"]):
            number = int(filteredString)
            MIN_RANGE = int(math.pow(-2,31))
            MAX_RANGE = int(math.pow(2,31))-1
            if (number<MIN_RANGE):
                number = MIN_RANGE
            if (number>MAX_RANGE):
                number = MAX_RANGE
        return number
print ("Solution\""+str(Solution().myAtoi("3.14159"))+"\"")