from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s == '' or numRows == 1:
            return s
        len_str = len(s)
        base = 2*(numRows-1)
        nums = len_str // base
        base_ind = [x for x in range(numRows)]

        minis = len_str % base
        print(nums)
        print(base_ind)
        print(base)
        print(minis)
        arr = defaultdict(list)
        for i in range(nums):
            for j in base_ind:
                if j in [base_ind[-1], base_ind[0]]:
                    arr[j].append(j+base*i)
                else:
                    arr[j].extend([j+base*i, j+base*(i+1)-2*j])

        flag = nums * base
        if minis != 0:
            if minis // numRows == 0:
                for i in range(0, minis):
                    arr[i].append(flag+i)
            else:
                for i in range(0, numRows):
                    arr[i].append(flag+i)
                for i, val in enumerate(range(flag+numRows, len_str), 1):
                    arr[numRows-i-1].append(val)
                    print(val)

        arr_str = defaultdict(list)
        for k in arr.keys():
            for i in arr[k]:
                arr_str[k].append(s[i])

        return ''.join([''.join(val) for val in arr_str.values()])


if __name__ == "__main__":
    solution = Solution()
    string = 'LEETCODEISHIRING'
    numRows = 4
    # result = 'LCIRETOESIIGEDHN'

    '''
    string = 'LEETCODEISHIRING'
    numRows = 3
    # result = 'LDREOEIIECIHNTSG'
    '''
    result = solution.convert(string, numRows)

    print(result)
