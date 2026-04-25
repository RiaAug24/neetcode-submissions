class TreeNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class PrefixTree:
    def __init__(self):
        self.root = TreeNode()
      

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                continue
            return False

        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:

        cur = self.root

        for p in prefix:
            if p not in cur.children:
                return False
            cur = cur.children[p]
        return True


        
        