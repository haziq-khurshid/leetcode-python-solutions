class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head                       # Initializing two pointers at start
        for _ in range(n):                       # Take fast pointer to position "n"
            fast = fast.next
        if not fast: return head.next            # If fast pointer is at null, just remove first element and return head
        while fast.next != None:                 # When fast reaches end, slow will be at previous node of the node to be removed
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next               # Skip next node of slow
        return head