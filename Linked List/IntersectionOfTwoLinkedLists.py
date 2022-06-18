class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr1 = headA                                    # First pointer at head of A
        ptr2 = headB                                    # Second pointer at head of B
        while ptr1 != ptr2:                             # While both pointers don't meet, keep moving them forward
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            if ptr1 == ptr2: return ptr1                # If pointers meet, return the pointer node
            if ptr1 == None: ptr1 = headB               # If pointer 1 reaches end, place it at head of B
            if ptr2 == None: ptr2 = headA               # If pointer 2 reaches end, place it at head of A
        return ptr1