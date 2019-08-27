from typing import List
import math


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        left = (n + m + 1) // 2
        right = (n + m + 2) // 2

        return (get_median(nums1, 0, n-1, nums2, 0, m-1, left) +
                get_median(nums1, 0, n-1, nums2, 0, m-1, right)) / 2


def get_median(arr1, start1, end1, arr2, start2, end2, k):
    len1 = end1 - start1 + 1
    len2 = end2 - start2 + 1

    if len1 > len2:
        return get_median(arr2, start2, end2, arr1, start1, end1, k)
    if len1 == 0:
        return arr2[start2+k-1]

    if k == 1:
        return min(arr1[start1], arr2[start2])

    i = start1 + min(len1, k // 2) - 1
    j = start2 + min(len2, k // 2) - 1

    if arr1[i] > arr2[j]:
        return get_median(arr1, start1, end1, arr2, j+1, end2, k-(j-start2+1))
    else:
        return get_median(arr1, i+1, end1, arr2, start2, end2, k-(i-start1+1))


if __name__ == '__main__':
    solution = Solution()
    # nums1 = [1, 2, 7, 9]
    # nums2 = [3, 4]
    # nums1 = [1, 3]
    # nums2 = [2]
    # nums1 = []
    # nums2 = [1]
    nums1 = [4, 5, 6, 7]
    nums2 = [1, 2, 3]

    print(solution.findMedianSortedArrays(nums1, nums2))
