class Solution:
    def generateParenthesis(self, n: int):
        generatedParenthesis = {1:["()"]}
        for index in range(2,n+1):
            generatedParenthesis[index] = []
            for paranthesis in generatedParenthesis[index-1]:
                generatedParenthesis[index].append("()"+paranthesis)
                generatedParenthesis[index].append("("+paranthesis+")")
            for pastParanthesisindex in range(1,index-1):
                for pastParanthesis in generatedParenthesis[pastParanthesisindex]:
                    for nextParanthesis in generatedParenthesis[index-1-pastParanthesisindex]:
                        generatedParenthesis[index].append("("+pastParanthesis+")"+nextParanthesis)
        return generatedParenthesis[n]

print ("Solution\""+str(Solution().generateParenthesis(3))+"\"")
