# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None                # Return if list is empty
        size = 1                                # Variable to track length of list
        tail = head
        while tail.next:                        # Bring tail pointer at last node and keep track of length
            size += 1
            tail = tail.next
                                                # Subtracting input number from size gives the new position of current head
        for _ in range(size - k % size):        # Run loop till head reaches the desired position
            tail.next = head                    # Point tail to head
            head = head.next                    # Move head forward
            tail = tail.next                    # Move tail forward
            tail.next = None                    # Point next of tail to none so it doesn't create a cycle
        return head                             