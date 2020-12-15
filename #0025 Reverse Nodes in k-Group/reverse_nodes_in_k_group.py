# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        listNodeList = []
        node = head
        while node is not None:
            listNodeList.append(node)
            node = node.next
        
        index = 0
        len_listNodeList = len(listNodeList)
        while index+k<=len_listNodeList:
            subList = listNodeList[index:index+k]
            listNodeList = listNodeList[:index]+subList[::-1]+listNodeList[index+k:]
            index = index+k
        
        for index,node in enumerate(listNodeList):
            node.next = listNodeList[index+1] if index<len_listNodeList-1 else None
        
        return listNodeList[0] if listNodeList else None