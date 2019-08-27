# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         maxstr = ''
#         flag = 0
#         for i in range(len(s), 0, -1):
#             if flag == 1:
#                 break
#             for j in range(0, len(s)-i+1):
#                 substr = s[j: j+i]
#                 if substr == substr[::-1]:
#                     flag = 1
#                     maxstr = substr
#         return maxstr

class Solution:
    def longestPalindrome(self, s: str) -> str:
        flag = 0
        maxstr = ''
        for i in range(len(s), 0, -1):
            if flag == 1:
                break
            for j in range(0, len(s)-i+1):
                substr = s[j: j+i]
                if substr[0: i//2] == substr[i-i//2:][::-1]:
                    flag = 1
                    maxstr = substr
        return maxstr


if __name__ == "__main__":
    solution = Solution()
    string = 'babad'
    result = solution.longestPalindrome(string)

    print(result)
