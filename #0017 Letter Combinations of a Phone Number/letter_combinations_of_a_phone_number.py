class Solution:

    DIGITS_MAP = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz",
    }

    def find_permutations(self, str1, str2):
        perms = []
        for i in str1:
            for j in str2:
                perms.append(i+j)
        if not perms:
            return list(str1) if str1 else list(str2)
        return perms

    def letterCombinations(self, digits: str):
        perms = []
        for digit in digits:
            perms = self.find_permutations(perms,list(self.DIGITS_MAP.get(digit)))
        return perms

# Optimized Solution
# class Solution:
#     def letterCombinations(self, digits: str):
#         if not digits:
#             return []
#         res = [''] # need 1 empty element to start loop
#         h = {'0':'','1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'} # hash table
#         for d in digits:
#             res = [r + letter for r in res for letter in h[d] ] # sequentially add a subsequent letter
#         return res
            
print ("Solution\""+str(Solution().letterCombinations("23"))+"\"")