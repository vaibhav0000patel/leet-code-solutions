# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        data = []
        for node in lists:
            while node is not None:
                data.append(node)
                node = node.next
        data.sort(key=lambda x:x.val)
        data_len = len(data)
        for index,node in enumerate(data):
            node.next = data[index+1] if index<data_len-1 else None
        return data[0] if data else None
        
# class Solution:
#     def mergeKLists(self, lists) -> ListNode:
        
#         len_lists = len(lists)
#         sortedNodeHead = None
#         sortedNode = None
#         while True:
#             minNodeTup = None
#             for index in range(len_lists):
#                 if lists[index] is not None:
#                     if minNodeTup is None or (lists[index].val<minNodeTup[1].val):
#                         minNodeTup = (index,lists[index])
#             if not minNodeTup:
#                 break
#             if not sortedNode:
#                 sortedNode = minNodeTup[1]
#                 sortedNodeHead = sortedNode
#             else:
#                 sortedNode.next = minNodeTup[1]
#                 sortedNode = sortedNode.next
#             lists[minNodeTup[0]] = minNodeTup[1].next
#         return sortedNodeHead