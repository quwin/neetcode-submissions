# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or all(x == None for x in lists):
            return None
        k = len(lists)
        head = ListNode()
        curr = head
        while not all(x == None for x in lists):
            minVal, index = 1001, -2
            for i in range(k):
                if lists[i] and lists[i].val < minVal:
                    minVal = lists[i].val
                    index = i
            curr.next = lists[index]
            curr = curr.next
            lists[index] = lists[index].next

        return head.next