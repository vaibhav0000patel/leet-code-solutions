# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def addTwoNumbers(self, l1, l2):
        baseNode = None
        lastNode = None
        carry = 0
        while l1 is not None or l2 is not None:
            dsum = carry
            if l1:
                dsum+=l1.val
                l1 = l1.next
            if l2:
                dsum+=l2.val
                l2 = l2.next
            carry = 1 if dsum>=10 else 0
            currentNode = ListNode(dsum%10)
            if baseNode is None:
                baseNode = currentNode
                lastNode = currentNode
                continue
            lastNode.next = currentNode
            lastNode = lastNode.next
        if carry == 1:
            lastNode.next = ListNode(carry)
        return baseNode