# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Iterative Solution
        prev = None
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
        return prev
        """
        """ Recusrive Solution """
        if not head or not head.next: return head
        new_head = self.reverseList(head.next)              # Call recursive function with head starting from next node
        head.next.next = head                               # Reversing direction by pointing next of next to current node
        head.next = None                                    # And next of current to Null
        return new_head