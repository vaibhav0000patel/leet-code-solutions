# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sortedhead = None
        sortednode = None
        while l1!=None and l2!=None:
            node = None
            if l1.val<l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            if sortednode:
                sortednode.next = node
                sortednode = sortednode.next
            else:
                sortednode = node
                sortedhead = sortednode
        while l1!=None:
            node = ListNode(l1.val)
            if sortednode:
                sortednode.next = node
                sortednode = sortednode.next
            else:
                sortednode = node
                sortedhead = sortednode
            l1 = l1.next
        while l2!=None:
            node = ListNode(l2.val)
            if sortednode:
                sortednode.next = node
                sortednode = sortednode.next
            else:
                sortednode = node
                sortedhead = sortednode
            l2 = l2.next
        return sortedhead