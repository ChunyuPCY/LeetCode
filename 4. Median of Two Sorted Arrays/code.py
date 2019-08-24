from typing import List
import math


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m_index = []
        m_val = []
        l_1, l_2 = len(nums1), len(nums2)
        aver_len = (l_1 + l_2) // 2
        if (l_1 + l_2) % 2 == 0:
            m_index.extend([aver_len-2, aver_len-1])
        else:
            m_index.append(aver_len)
        # print("中位数在整体数组中的索引位置：", m_index)
        p_l1, p_l2, cur = 0, 0, 0

        while p_l1 < l_1 and p_l2 < l_2:
            if nums1[p_l1] < nums2[p_l2]:
                p_l1 += 1
            else:
                p_l2 += 1
            cur += 1
            if cur > int(math.fsum(m_index)):
                break
        # print('cur:', cur, '\np_l1:', p_l1, '\np_l2:', p_l2)
        if cur <= int(math.fsum(m_index)):  # 说明两个数组，至少有一个数组已经扫描结束
            if p_l2 == l_2:
                p_l2 = p_l2 - 1
                temp = nums2[p_l2]
                arr = nums1
                p = int(math.fsum(m_index)) - p_l2
            else:
                p_l1 = p_l1 - 1
                temp = nums1[p_l1]
                arr = nums2
                p = int(math.fsum(m_index)) - p_l1

            flag, ind = 0, 0
            print(m_index)
            print(p)
            for i in range(len(m_index)):
                if (flag == 0) and min(arr[p + ind], temp) == temp:
                    flag = 1
                    m_val.append(temp)
                else:
                    m_val.append(arr[p + ind])
                    ind += 1
        else:
            #  说明中位数在两个指针前部，两个数组的指针都没有扫描结束
            if p_l1 == l_1:
                p_l1 = l_1 - 1
            else:
                p_l2 = l_2 - 1
            m_val.append(min(nums1[p_l1], nums2[p_l2]))
            if len(m_index) > 1:
                m_val.append(max(nums1[p_l1], nums2[p_l2]))

        return math.fsum(m_val) / len(m_val)


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 7, 9]
    nums2 = [3, 4]
    # nums1 = [1, 3]
    # nums2 = [2]
    # nums1 = []
    # nums2 = [1]

    print((solution.findMedianSortedArrays(nums1, nums2)))

