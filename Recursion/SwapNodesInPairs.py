# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:              
            return head
        second = head.next                          # Second node would be next of head
        head.next = self.swapPairs(second.next)     # Next of head would be starting node of next pair
        second.next = head                          # Next of second would be head
        return second                               # Return second node as new head