class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """Solution"""
        """                        # Below Solution takes values in a list and compares if the reverse order matches actual order
        nums = []                               
        while head:
            nums.append(head.val)
            head = head.next
        return nums == nums[::-1]
        """
        
        """Follow up Solution"""        # Below is solution for O(n) time and O(1) space
        slow = fast = head              # Start two pointers and find mid of linked list by moving fast in double steps
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        curr = None     
        while slow:                     # Once slow pointer is at mid, reverse rest of the linked list
            temp = slow.next
            slow.next = curr
            curr = slow
            slow = temp
        while curr:                     # Compare reversed second half with original first half
            if head.val != curr.val:
                return False            # If some value doesn't matches, it isn't a palindrome
            curr = curr.next
            head = head.next
        return True