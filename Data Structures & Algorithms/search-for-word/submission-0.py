class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit_path = set()

        def dfs(r, c, i):
            if i == len(word): return True
            if r < 0 or r > len(board) - 1 or c < 0 or c > len(board[0]) - 1 or board[r][c] != word[i] or (r,c) in visit_path:
                return False

            if board[r][c] == word[i]:
                i += 1

            visit_path.add((r,c))

            res = (dfs(r-1, c, i) or
                dfs(r+1, c, i) or
                dfs(r, c-1, i) or
                dfs(r, c+1, i))

            visit_path.remove((r, c))
            
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False




        


        