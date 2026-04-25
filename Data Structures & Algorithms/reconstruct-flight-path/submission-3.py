class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}

        tickets.sort()
        for src, dest in tickets:
            if src in adj:
                adj[src].append(dest)
            else:
                adj[src] = [dest]
        
        res = ['JFK']
        n = len(tickets)

        def dfs(src):
            
            if len(res) == n + 1:
                return True

            if src not in adj:
                return False

            tmp = list(adj[src])

            for i, v in enumerate(tmp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True

                res.pop()
                adj[src].insert(i, v)

            return False

        dfs('JFK')
        return res



    
        