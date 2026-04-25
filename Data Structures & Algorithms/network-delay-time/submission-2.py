class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        adjMap = {i:[] for i in range(1, n+1)}

        for node, edge, time in times:
            adjMap[node].append([edge, time])
        
        
        visit = [0] * n
        q = [[0, k]]

        while q:
            heapq.heapify(q)
            time, node  = heapq.heappop(q)
            if not visit[node-1]:
                visit[node-1] = 1
                for nei, t in adjMap[node]:
                    heapq.heappush(q, [time+t, nei])
                res = time
                
        return res if visit.count(1) == n else -1

            




        