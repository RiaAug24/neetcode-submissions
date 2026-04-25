class MedianFinder:

    def __init__(self):
        self.stream = []
        self.n = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.stream, num)
        self.n += 1
    def findMedian(self) -> float:
        count = 0
        temp = self.stream.copy()
        if self.n % 2 != 0:
            while count != self.n // 2:
                heapq.heappop(temp)
                count += 1
            med = heapq.heappop(temp)
        else:
            while count != (self.n // 2) - 1:
                heapq.heappop(temp)
                count += 1
            num1 = heapq.heappop(temp)
            num2 = heapq.heappop(temp)
            med = (num1 + num2) / 2
        return med


        
        