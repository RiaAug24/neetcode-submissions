from itertools import combinations
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtracking(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtracking(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtracking(openN, closeN + 1)
                stack.pop()
            
            return
        backtracking(0, 0)
        return res



    #     res = set()
    #     comb_of_parenthesis = list(combinations("()" * 2 * n, n * 2))
    #     for x in comb_of_parenthesis:
    #         par_str = ""
    #         for i in range(0, len(x)):
    #             par_str += x[i]
    #         valid = self.validate(par_str)
    #         if valid:
    #             res.add(par_str)
    #     return list(res)
    # def validate(self, par_str):
    #     stk = []
    #     for x in par_str:
    #         if x == ")":
    #             if len(stk) == 0:
    #                 return False
    #             else:
    #                 stk.pop()
    #                 continue
    #         stk.append(x)
    #     if len(stk) == 0:
    #         return True
    #     else:
    #         return False



        

        

    



        