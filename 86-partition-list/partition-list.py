# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        # Dummy nodes to serve as start anchors
        before_head = ListNode(0)
        after_head = ListNode(0)
        
        # Pointers to track the end of both lists
        before = before_head
        after = after_head
        
        curr = head
        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            curr = curr.next
        
        # Break potential cycle at the end of the 'after' list
        after.next = None
        
        # Connect the two partitions
        before.next = after_head.next
        
        return before_head.next