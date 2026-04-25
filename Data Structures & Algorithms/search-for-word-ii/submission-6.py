class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        visit = set()
        ROWS = len(board)
        COLS = len(board[0])
        res = set()
        def dfs(r, c, word, root):

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] not in root.children or (r, c) in visit:
                return
       
            visit.add((r, c))
            word += board[r][c]
            root = root.children[board[r][c]]

            if root.end:
                res.add(word)
            
            dfs(r+1, c, word, root)
            dfs(r-1, c, word, root)
            dfs(r, c+1, word, root)
            dfs(r, c-1, word, root)

            visit.remove((r, c))
            
            
        root = TrieNode()
        for word in words:
            cur = root
            for w in word:
                if w not in cur.children:
                    cur.children[w] = TrieNode()
                cur = cur.children[w]
            cur.end = True

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", root)
        return list(res)

   


        