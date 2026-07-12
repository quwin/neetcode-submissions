# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        top = ListNode()
        dummy = None
        
        while head != None:
            dummy = top.next
            top.next = head
            head = head.next
            top.next.next = dummy

        return top.next