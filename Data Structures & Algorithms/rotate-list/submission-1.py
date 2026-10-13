# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        right = head
        length = 1
        while right.next != None:
            right = right.next
            length += 1
        right.next = head

        if k >= length:
            k %= length

        for _ in range(0, length-k-1):
            head = head.next if head else None
        
        newHead = head.next
        head.next = None
        
        return newHead

