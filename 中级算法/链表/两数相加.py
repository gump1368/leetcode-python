"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        out = ListNode(-1)
        recoder = out
        overflow = 0
        x1 = l1.val
        x2 = l2.val
        while 1:
            sum_ = x1 + x2 + overflow
            if sum_ >= 10:
                val = sum_ - 10
                overflow = 1
            else:
                val = sum_
                overflow = 0
            node = ListNode(val)
            recoder.next = node
            recoder = recoder.next

            if l1.next:
                l1 = l1.next
                x1 = l1.val
            else:
                x1 = 0

            if l2.next:
                l2 = l2.next
                x2 = l2.val
            else:
                x2 = 0

            if l1.next is None and l2.next is None and overflow == 0 and x1 == 0 and x2 == 0:
                break

        return out.next