class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: 
            return head                     # If list contains less than 2 elements, return list
        odd = head                          # Place odd pointer at start   
        even = even_head = head.next        # Place even pointer at next of start and also keep track of head of even pointer
        while even and even.next:           # Traverse through list by skipping one node for both odd and even pointers
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head                # Point next off odd pointer to start of even pointer, so they are linked
        return head                         # Return head