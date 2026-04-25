import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        merged_sorted_arr = []
        n = len(nums1)
        m = len(nums2)
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                merged_sorted_arr.append(nums1[i])
                i += 1
            else:
                merged_sorted_arr.append(nums2[j])
                j += 1
        while i < n:
            merged_sorted_arr.append(nums1[i])
            i += 1
        while j < m:
            merged_sorted_arr.append(nums2[j])
            j += 1
        if (n + m) % 2 == 0:
            return (merged_sorted_arr[math.floor((n + m) / 2 )] + merged_sorted_arr[math.floor((n + m - 1) / 2 )]) / 2
        else:
            return merged_sorted_arr[math.floor((n + m) / 2 )]
