class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()  # i - j
        diag2 = set()

        res = []
        board = []

        def dfs(i):
            if i == n:
                res.append(board.copy())
                return
         
            for j in range(n):
                if j in cols or (i - j) in diag1 or (i + j) in diag2:
                    continue
                
                cols.add(j)
                diag1.add(i - j)
                diag2.add(i + j)
                board.append("." * j + "Q" + "." * (n - j - 1))
                
                dfs(i+1)
                
                cols.remove(j)
                diag1.remove(i - j)
                diag2.remove(i + j)
                board.pop()
                
        dfs(0)
        return res

    # def checkNoAttk(self, board):
    #       # i + j

    #     for i in range(n):
    #         for j in range(n):
    #             if board[i][j] == 'Q':
    #                 if j in cols or (i - j) in diag1 or (i + j) in diag2:
    #                     return False
    #                 cols.add(j)
    #                 diag1.add(i - j)
    #                 diag2.add(i + j)
    #     return True
            
        
        





            

