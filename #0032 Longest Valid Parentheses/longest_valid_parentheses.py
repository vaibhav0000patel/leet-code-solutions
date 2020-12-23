class Solution:

    def longestValidParentheses(self, s: str) -> int:
        OPENING = ["("]
        CLOSING = [")"]

        dp = [0]*len(s)
        longest_length = 0
        for index in range(1,len(s)):
            if s[index] in CLOSING:
                last_index_ref = index - dp[index-1]
                if s[index-1] in OPENING:
                    dp[index] = dp[index-2]+2 if index>=2 else 2
                elif (last_index_ref>0 and s[last_index_ref-1] in OPENING):
                    dp[index] = dp[index-1] + (dp[last_index_ref-2]+2 if last_index_ref>=2 else 2)
                longest_length = max(longest_length,dp[index])
        return longest_length


    # def longestValidParentheses(self, s: str) -> int:
    #     OPENING = ["(","[","{"]
    #     CLOSING = [")","]","}"]

    #     longest_length = 0
    #     stack = []
    #     length = 0
    #     is_valid = False
    #     for indexi in range(len(s)):
    #         if s[indexi] in OPENING:
    #             stack.append(s[indexi])
    #         else:
    #             if not stack or stack[-1]!=OPENING[CLOSING.index(s[indexi])]:
    #                 if length>longest_length:
    #                     longest_length = length
    #                 length = 0
    #                 stack = []
    #             else:
    #                 stack.pop()
    #                 length+=2
    #         if length>longest_length:
    #             longest_length = length
    #     return longest_length

print ("Solution\""+str(Solution().longestValidParentheses("()(()"))+"\"")