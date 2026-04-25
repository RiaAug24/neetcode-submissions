class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for x in stones:
            heapq.heappush(maxHeap, -x)
        while len(maxHeap) > 1:
            x, y = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            if x < y:
                heapq.heappush(maxHeap, -(y - x))
            elif x > y:
                heapq.heappush(maxHeap, -(x - y))
            else:
                continue
        if maxHeap:
            return -maxHeap[0]
        return 0



        