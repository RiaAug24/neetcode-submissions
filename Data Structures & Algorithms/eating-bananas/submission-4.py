import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        min_k = float('inf')
        l = 1
        r = max(piles)
        while l <= r:
            k = int((l + r) / 2)
            i = h_taken = 0
            while i < n:
                h_taken += math.ceil(piles[i] / k)
                i += 1
            if h_taken <= h:
                min_k = min(min_k, k)
                r = k - 1
            else:
                l = k + 1
        return min_k
            





        