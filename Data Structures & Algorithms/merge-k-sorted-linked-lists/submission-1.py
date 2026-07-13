# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Wrapper:
    def __init__(self, node: ListNode):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

    def __le__(self, other):
        return self.node.val <= other.node.val
    
    def __ge__(self, other):
        return self.node.val >= other.node.val

    def __gt__(self, other):
        return self.node.val > other.node.val
    
    def __eq__(self, other):
        return self.node.val == other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or all(x == None for x in lists):
            return None

        heap = []
        for node in lists:
            heapq.heappush(heap, Wrapper(node))

        head = ListNode()
        curr = head

        while heap:
            wrapper = heapq.heappop(heap)
            curr.next = wrapper.node
            curr = curr.next

            if curr.next:
                heapq.heappush(heap, Wrapper(curr.next))

        return head.next