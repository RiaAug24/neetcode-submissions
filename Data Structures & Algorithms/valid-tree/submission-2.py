class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = {}
        for node, e in edges:
            if e in adjMap:
                adjMap[e].append(node)
            elif node in adjMap:
                adjMap[node].append(e)
            else:
                adjMap[node] = [e]
        print(adjMap)

        visit = [0] * n
        flag = False
        def dfs(node):
            if node not in adjMap:
                visit[node] = 1
                return

            if visit[node]:
                return

            for c in adjMap[node]:
                if c == node or visit[c]:
                    flag = True
                    return
                dfs(c)

            visit[node] = 1
        
        dfs(0)

        
        if visit.count(1) != n or flag:
            return False
        return True
        
        
            

        
        