# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#       return [i, j]
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums:
        :param target:
        :return:
        """
        seen = {}
        for i, v in enumerate(nums):

            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]

            seen[v] = i

        return []


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9

    result = solution.twoSum(nums, target)

    print(result)
