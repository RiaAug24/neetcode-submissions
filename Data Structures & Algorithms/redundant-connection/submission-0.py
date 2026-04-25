class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        res = []

        def dfs(node, visit, adjMap):
            if visit[node-1]:
                return
            
            visit[node-1] = 1

            for c in adjMap[node]:
                dfs(c, visit, adjMap)
            
        for x in edges:
            visit = [0] * n
            adjMap = {i: [] for i in range(1, n+1)}
            for node, e in edges:
                if x != [node, e]:
                    if e not in adjMap[node]: adjMap[node].append(e)
                    if node not in adjMap[e]: adjMap[e].append(node)

            dfs(1, visit, adjMap)
            if visit.count(1) == n:
                res = x
        return res


        