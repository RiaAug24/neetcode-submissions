class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        ch_map = {str(i):chr(ch) for ch, i in zip(range(ord('A'), ord('Z')+1), range(1, 27)) }
        if s[0] == '0': return 0
        group = []
        
        def dfs(i, arr):
            if i >= n:
                temp = arr.copy()
                if temp not in group:
                    group.append(temp)
                return
            

            if s[i] in ch_map:
                arr.append(s[i])
                dfs(i+1, arr)
                arr.pop()

            if s[i:i+2] in ch_map:
                arr.append(s[i:i+2])
                dfs(i+2, arr)
                arr.pop()
            
        dfs(0, [])

        return len(group)





