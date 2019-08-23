from typing import List
import json

class ListNode:
    """ Definition for singly-linked list. """
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(l1.val + l2.val)
        ptr = head
        flag = 0
        while (l1 is not None) and (l2 is not None):
            add_value = l1.val + l2.val + flag
            if add_value >= 10:
                flag = 1
                ptr.val = add_value - 10
            else:
                flag = 0
                ptr.val = add_value

            l1, l2 = l1.next, l2.next
            if (l1 is not None) or (l2 is not None):
                ptr.next = ListNode(-1)
                ptr = ptr.next

        if l1 is None:
            l1 = l2

        if l1 is not None:
            if flag == 1:
                while l1 is not None:
                    add_value = l1.val + flag
                    if add_value >= 10:
                        flag = 1
                        ptr.val = add_value - 10
                    else:
                        flag = 0
                        ptr.val = add_value
                    l1 = l1.next
                    if l1 is not None:
                        ptr.next = ListNode(-1)
                        ptr = ptr.next
            else:
                ptr.val = l1.val
                ptr.next = l1.next

        if flag == 1:
            ptr.next = ListNode(1)

        return head


def stringToIntegerList(input):
    return json.loads(input)  # list object


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next

    # print(result)
    return "[" + result[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line)
            line = next(lines)
            l2 = stringToListNode(line)

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
