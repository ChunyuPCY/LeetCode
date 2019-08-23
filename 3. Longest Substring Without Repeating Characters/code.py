class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w_size = 1
        start = 0

        maxlen = 0

        while w_size <= len(s):
            substr = s[start: w_size + start]
            if len(set(substr)) < len(substr):
                if w_size + start == len(s):
                    break
                start += 1
            else:
                maxlen += 1
                w_size += 1
                start = 0

        return maxlen


if __name__ == '__main__':
    solution = Solution()
    # string = "bbbbbb"
    string = "abcabcbb"
    # string = "pwwkew"
    print((solution.lengthOfLongestSubstring(string)))

