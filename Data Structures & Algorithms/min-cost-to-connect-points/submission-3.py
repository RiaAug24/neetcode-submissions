class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        adjPt = {i:[] for i in range(n)}
        
        for i in range(n):
            x1, y1 = points[i] 
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                adjPt[i].append([dist, j])
                adjPt[j].append([dist, i])
        
        visit = set()
        minHeap = [[0, 0]]
        res = 0
        
        while len(visit) != n:
            dist, i = heapq.heappop(minHeap)

            if i in visit:
                continue
            
            res += dist
            visit.add(i)
            for neiCost, nei in adjPt[i]:
                heapq.heappush(minHeap, [neiCost, nei])

       
  

        return res
            