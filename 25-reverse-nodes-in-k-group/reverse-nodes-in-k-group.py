# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k == 1:
            return head

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # 1. Find the k-th node from groupPrev
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next

            # 2. Reverse the k nodes in this group
            prev = kth.next
            curr = groupPrev.next
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # 3. Connect groupPrev to the new head of the reversed group
            tmp = groupPrev.next  # tmp becomes the tail of the newly reversed group
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        """Helper to find the k-th node starting from curr."""
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr  