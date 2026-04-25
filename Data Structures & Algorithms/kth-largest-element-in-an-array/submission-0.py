class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)
        c = 1
        while c != k:
            heapq.heappop(maxHeap)
            c += 1
        res = heapq.heappop(maxHeap)
        return -res