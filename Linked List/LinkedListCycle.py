""" Below is the code to find out if 
    a Linked List contains a cycle. """

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head                          # Initialize two containers at start
        while fast and fast.next:                   # While end of linked list is not found
            slow = slow.next                        # Move slow pointer one step
            fast = fast.next.next                   # Move fast pointer two steps
            if slow == fast:                        # If both pointers ever meet, it means there is a cycle
                return True
        return False