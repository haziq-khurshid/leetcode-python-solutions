class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None                                    # Point previous pointer to null
        while head:                                    # While end of linked list is not reached
            current = head                             # Point current pointer to head
            head = head.next                           # Move head a step forward
            current.next = prev                        # Point next of current pointer to previous
            prev = current                             # Bring previous to current's position
        return prev                                    # Return previous as it will have reveresed linked list