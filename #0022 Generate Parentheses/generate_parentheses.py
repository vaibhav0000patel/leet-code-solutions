class Solution:
    def generateParenthesis(self, n: int):
        listOfParentheses = []
        
        parentheses = "".join(["("]*n+[")"]*n)
        listOfParentheses.append(parentheses)

        while "))" in parentheses:
            index = parentheses.index("))")
            parentheses = parentheses[:index-1]+ parentheses[index] + parentheses[index-1:index] + parentheses[index+1:]
            if parentheses not in listOfParentheses:
                listOfParentheses.append(parentheses)

        parentheses = "".join(["("]*n+[")"]*n)
        while "((" in parentheses: 
            index = parentheses.rindex("((")
            parentheses = parentheses[:index+1] + parentheses[index+2:index+3] + parentheses[index+1]  + parentheses[index+3:]
            if parentheses not in listOfParentheses:
                listOfParentheses.append(parentheses)

        return listOfParentheses

print ("Solution\""+str(Solution().generateParenthesis(3))+"\"")


Input
4
Output
["(((())))","((()()))","((())())","(()()())","(()())()","(())()()","()()()()","(()(()))","()(()())","()()(())"]
Expected
["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]