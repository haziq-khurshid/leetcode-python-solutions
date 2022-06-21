class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None: return None         # If both lists are empty, return None
        dummy_head = ListNode(-1)                      # Initializing dummy head to keep track of sorted nodes
        curr = dummy_head
        
        while list1 and list2:                        # Traverse through both lists
            if list1.val <= list2.val:                # If list1 has smaller value, move curr pointer to it
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2                     # If list2 has smaller value, move curr pointer to it
                list2 = list2.next
            curr = curr.next
            
        if list1:                                     # If list2 reached end, point current pointer to list1
            curr.next = list1
        else:
            curr.next = list2                         # If list1 reached end, point current pointer to list2
        
        return dummy_head.next                        # Return next of dummy head because it will be actual first node