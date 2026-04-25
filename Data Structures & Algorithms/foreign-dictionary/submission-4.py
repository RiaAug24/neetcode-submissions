class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Post order DFS AKA Topological Sort

        adj = { c: set() for w in words for c in w }

        for i in range(len(words)-1):

            word1, word2 = words[i], words[i+1]
            m, n = len(word1), len(word2)
            min_len = min(m, n)
            if m > n and word1[:min_len] == word2:
                return ""
            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
        print(adj)
        visit = {}
        res = []

        def dfs(ch):
            if ch in visit:
                return visit[ch]
            
            visit[ch] = True

            for nei in adj[ch]:
                if dfs(nei):
                    return True
            
            visit[ch] = False
            res.append(ch)

            return False

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)
