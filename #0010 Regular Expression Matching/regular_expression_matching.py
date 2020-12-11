class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pindex = 0
        sindex = 0
        if "*" not in s and len(s)!=len(p):
            return False
        while sindex<len(s):
            if s[sindex]!=p[pindex] and p[pindex]!=".":
                return False
            if sindex<len(s)-1:
                if s[sindex+1]==s[sindex]:
                    if not (pindex<len(p)-1):
                        return False
                    if s[sindex+1]!=p[pindex+1] and p[pindex+1]!="*" and p[pindex]!=".":
                        return False
                    if s[sindex+1]==p[pindex+1] or (p[pindex]=="." and p[pindex+1]!="*"):
                        pindex+=1
                else:
                    if(p[pindex]=="." and p[pindex+1]!="*"):
                        pindex+=1
                    if p[pindex]=="*":
                        pindex+=1
                    if not (pindex<len(p)):
                        return False
                    if s[sindex+1]!=p[pindex]:
                        return False
            sindex += 1
        return True
print ("Solution\""+str(Solution().isMatch("mississippi","mis*is*p*."))+"\"")