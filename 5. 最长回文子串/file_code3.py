class Solution:
    # 马拉车算法
    def longestPalindrome(self, s: str) -> str:
        T = preprocess(s)
        n = len(T)
        C, R = 0, 0
        P = [0] * n

        for i in range(1, n-1):
            i_mirror = 2 * C - i
            P[i] = min(R-i, P[i_mirror]) if R > i else 0

            while T[i-1-P[i]] == T[i+1+P[i]]:
                P[i] += 1

            if i + P[i] > R:
                C = i
                R = P[i] + i

        maxlen = 0
        center_index = 0
        for i in range(1, n-1):
            if P[i] > maxlen:
                maxlen = P[i]
                center_index = i

        start_index = (center_index - maxlen) // 2
        return s[start_index: maxlen + start_index]


def preprocess(s: str):
    temp_str = ''
    for i in s:
        temp_str += '#' + i

    temp_str = '^' + temp_str + '#$'
    return temp_str

if __name__ == "__main__":
    solution = Solution()
    # string = 'cbbd'
    string = 'babad'

    result = solution.longestPalindrome(string)

    print(result)
