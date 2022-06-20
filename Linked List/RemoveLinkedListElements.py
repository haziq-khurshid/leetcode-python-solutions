class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None: return head                        # Return head if linked list is empty
        while head and head.val == val:                     # If value is at start, keep moving head forward
            head = head.next
        temp = head
        while temp and temp.next:                           # While end of list is not reached
            if temp.next.val == val:                        # If value of next node is equal to input value
                temp.next = temp.next.next                  # Skip next node
            else:
                temp = temp.next                            # Else move to next node
        return head