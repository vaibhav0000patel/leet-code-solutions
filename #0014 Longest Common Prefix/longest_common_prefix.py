class Solution(object):

    def commonPrefix(self,str1,str2):
        cp = ""
        for index in range(min(len(str1),len(str2))):
            if str1[index]!=str2[index]:
                return cp
            cp += str1[index]
        return cp

    def longestCommonPrefix(self, strs):
        if len(strs)<=1:
            return "" if not strs else strs[0]
        lcp = strs[0]
        for cstr in strs[1:]:
            lcp = self.commonPrefix(lcp,cstr)
            if not lcp:
                return lcp
        return lcp

print ("Solution\""+str(Solution().longestCommonPrefix(["flower","flow","flight"]))+"\"")