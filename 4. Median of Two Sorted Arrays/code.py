from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m_index = []
        l_1, l_2 = len(nums1), len(nums2)
        aver_len = l_1 + l_2 // 2
        if aver_len == 0:
            m_index.extend([aver_len-1, aver_len])
        else:
            m_index.append(aver_len)


'''
test
'''



if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]

    print((solution.findMedianSortedArrays(nums1, nums2)))

