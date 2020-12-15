# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self,node1,node2):
        node1 = node2.next
        _node = None if node1.next is None else node1.next
        node1.next = node2
        node2.next = _node
        return node1,node2

    def swapPairs(self, head: ListNode) -> ListNode:
        node = head
        lastNode = None
        while node is not None:
            if node.next is not None:
                if lastNode is None:
                    head,node = self.swapNodes(head,node)
                else:
                    lastNode.next,node = self.swapNodes(lastNode.next,node)
            lastNode = node
            node = node.next
        return head