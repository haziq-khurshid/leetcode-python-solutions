# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = current = ListNode(0)               # Initializing a dummy node to track new linked list
        carry = 0               
        while l1 or l2 or carry:                    # Run until both lists are traversed and carry is also zero           
            if l1:
                carry += l1.val                     # Add value of list 1 node in carry
                l1 = l1.next
            if l2:
                carry += l2.val                     # Add value of list 2 node in carry
                l2 = l2.next            
            current.next = ListNode(carry % 10)     # Take mod of carry and create a new node with the value
            current = current.next                  # Move current pointer to new node
            carry //= 10                            # Divide carry by 10, remainder will be carried to next iteration
        
        return dummy.next                           # Return list starting from next node of dummy node from start