class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        stk = []
        parentheses_map = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }


        for x in s:
            if x in parentheses_map.values():
                if len(stk) != 0 and parentheses_map[stk[-1]] == x:
                    stk.pop()
                    continue
                else:
                    return False
            stk.append(x)
        if len(stk) == 0:
            return True
        else:
            return False

        