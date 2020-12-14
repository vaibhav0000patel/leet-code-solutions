class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        currentNode = head
        nodeList = [currentNode]
        while(currentNode.next!=None):
            currentNode = currentNode.next
            nodeList.append(currentNode)
        if len(nodeList)<=1:
            return None
        if len(nodeList)-n<=0:
            return nodeList[-n].next
        nodeList[-n-1].next = nodeList[-n].next
        return head
            
        