class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidDist = {}
        origin = [0, 0]
        for x in points:
            exp = math.pow(x[0] - origin[0], 2) + math.pow(x[1] - origin[1], 2)
            dist = math.sqrt(exp)
            if dist in euclidDist:
                euclidDist[dist].append(x)
                continue
            euclidDist[dist] = deque([x])
        dists = list(euclidDist.keys())
        heapq.heapify(dists)
        c = 0
        res = []
        while c < k:
            dist = heapq.heappop(dists)
            if len(euclidDist[dist]) > 1:
                heapq.heappush(dists, dist)
            res.append(euclidDist[dist].popleft())
            c += 1
        return res
            
        