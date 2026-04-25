import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        A, B = nums1, nums2
        if n > m:
            A, B = B, A
        l, r = 0, len(A) - 1
        half = (n + m) // 2
        while True:
            mid1 = (l + r) // 2
            mid2 = half - mid1 - 2
            Aleft = A[mid1] if mid1 >= 0 else float('-inf')
            Aright = A[mid1 + 1] if (mid1 + 1) < len(A) else float('inf')
            Bleft = B[mid2] if mid2 >= 0 else float('-inf')
            Bright = B[mid2 + 1] if (mid2 + 1) < len(B) else float('inf')
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if (n + m) % 2 != 0:
                    return min(Aright, Bright)
                # even length
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = mid1 - 1
            else:
                l = mid1 + 1





              
        
