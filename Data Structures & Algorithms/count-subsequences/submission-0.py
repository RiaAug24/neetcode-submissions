class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        count = 0
        def backtrack(i, cur):
            
            nonlocal count

            if "".join(cur) == t:
                count += 1
                return

            if i == len(s) or len(cur) > len(t):
                return


            cur.append(s[i])
            backtrack(i+1, cur)
            cur.pop()
            backtrack(i+1, cur)
        
        backtrack(0, [])

        return count


        