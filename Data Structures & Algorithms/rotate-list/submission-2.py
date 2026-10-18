# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        curr = head
        length = 1
        while curr and curr.next:
            length += 1
            curr = curr.next
        curr.next = head
        curr = head
        k = length - (k % length) - 1
        for _ in range(k):
            curr = curr.next
        head = curr.next
        curr.next = None

        return head