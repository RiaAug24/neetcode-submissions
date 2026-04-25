class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = {i: [] for i in range(n)}

        for node, e in edges:
            if e not in adjMap[node]:
                adjMap[node].append(e)

            if node not in adjMap[e]:
                adjMap[e].append(node)

        print(adjMap)
        visit = [False] * n

        def dfs(node):
            print(node)
            
            if node not in adjMap:
                visit[node] = True
                return
                
            visit[node] = True

            for c in adjMap[node]:
                if not visit[c]:
                    dfs(c)
            

        res = 0
        for node in range(n):
            if not visit[node]:
                res += 1
                dfs(node)
            print(visit)
        return res

