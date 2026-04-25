class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        for sr, dt, cost in flights:
            adj[sr].append([dt, cost])
        
        print(adj)

        res = float('inf')

        visit = set()
        def dfs(src, price, i):
            nonlocal res
            print(visit)
            if src == dst and i <= k + 1:
                res = min(res, price)
                return
            
            if src in visit or i > k:
                return

            visit.add(src)

            for nei, cost in adj[src]:
                dfs(nei, price + cost, i+1)
            
            visit.remove(src)
            
            
        dfs(src, 0, 0)
        return res if res != float('inf') else -1

        