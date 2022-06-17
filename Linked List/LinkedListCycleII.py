""" Below is the code to find out at which 
    node a cycle starts in a Linked List. """

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head                          # Initialize two containers at start
        while fast and fast.next:                   # While end of linked list is not found
            slow = slow.next                        # Move slow pointer one step
            fast = fast.next.next                   # Move fast pointer two steps
            if slow == fast:                        # If both pointers ever meet, it means there is a cycle
                slow = head                         # Bring one pointer to start
                while slow != fast:                 # While both pointers don't meet, keep moving them ahead
                    slow = slow.next
                    fast = fast.next
                return slow                         # Return the node where both pointers meet this time
        return None