class Solution:
    # 中心匹配
    def longestPalindrome(self, s: str) -> str:
        if s == '' and s is None:
            return ''
        start, end = 0, 0
        for i in range(len(s)):
            len1 = expendstr(s, i, i)
            len2 = expendstr(s, i, i+1)
            maxlen = max(len1, len2)
            # print(len1, len2)
            if maxlen > end - start:
                start = i - (maxlen-1)//2
                end = i + maxlen // 2 + 1
                # print(maxlen, start, end)

        return s[start: end]


def expendstr(s: str, left: int, right: int):
    L, R = left, right
    while L >= 0 and R < len(s) and s[L] == s[R]:
        L, R = L - 1, R + 1

    return R - L - 1


if __name__ == "__main__":
    solution = Solution()
    # string = 'cbbd'
    string = 'a'

    # print(expendstr('abba', 1, 2))
    result = solution.longestPalindrome(string)

    print(result)
