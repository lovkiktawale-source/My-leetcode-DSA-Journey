# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next and prev.next.next:
            # Nodes to be swapped
            first = prev.next
            second = prev.next.next
            
            # Swapping pointers
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move prev pointer two steps forward for the next pair
            prev = first
            
        return dummy.next