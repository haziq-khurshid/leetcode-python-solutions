class Node:                             # Node class to initialize nodes of linked list
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):                                                 # Constructor for linked list
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:                           
        if index < 0 or index >= self.size: return -1                   # If index requested is out of range, return -1
        current = self.head
        for i in range(0,index):                                        # Traverse from starting index to the requested indes
            current = current.next
        return current.val                                              # Return value on that index

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)      

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: return
        current = self.head
        new_node = Node(val)                                            # Create a new node to be added

        if index <= 0:                                                  # If index is at start, Add node at the start
            new_node.next = current
            self.head = new_node
        else:
            for i in range(index - 1):                                 # Traverse till the previous node of requested index
                current= current.next
            new_node.next = current.next                               # Point next of new node to next of current node
            current.next = new_node                                    # Point next of current node to the new node
        self.size+=1                                                   # Increase size of linked list

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: return                     # If index is out of range, return
        current = self.head
        if index == 0:                                                 # If deletion needed at head, point head to next node
            self.head = self.head.next
        else:
            for i in range(0,index-1):
                current =current.next                                  # Else go to previous node of requested index
            current.next = current.next.next                           # Point current node to next of next node, Thus skipping next node from linked list
        self.size-=1                                                   # Decrease size of linked list

    def print_list(self) -> None:                                      # This function is just for testing purposes, to print the linked list
        current = self.head
        while current != None:
            print(current.val, " ")
            current = current.next


def main():
    linked_list = MyLinkedList()            # Linked List initialized
    """Call all the declared functions by changing the inputs in arguments
        and then verify the result by printing the linked list"""
    linked_list.addAtHead(3)
    linked_list.addAtTail(2)
    linked_list.addAtIndex(1,4)
    linked_list.deleteAtIndex(0)
    linked_list.print_list()

if __name__ == "__main__":
    main()