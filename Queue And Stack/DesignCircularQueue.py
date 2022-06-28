class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [0] * k                     # Initialzing queue with Zeroes
        self.size = k                           # Setting size equal to 'k' from input
        self.head = 0                           # Setting head to start
        self.count = 0                          # Setting count to zero
        

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.data[(self.head + self.count) % self.size] = value     # Add value at index where index is sum of head & count,
                                                                    # using mod becaus of circular queue
        self.count+=1                                               # Increase count of queue after adding new element
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = (self.head + 1) % self.size                     # Take head to next index
        self.count -= 1                                             # Decrease count of queue after deletion of element
        return True

    def Front(self) -> int:
        if not self.count: return -1
        return self.data[self.head]                                # Return value where index is equal to head position
        

    def Rear(self) -> int:
        if not self.count: return -1
        return self.data[(self.head + self.count - 1) % self.size]  # Return value where index equals 'head + count -1'
        

    def isEmpty(self) -> bool:                  
        return self.count == 0                                      # If count is 0, queue is empty

    def isFull(self) -> bool:
        return self.count == self.size                              # If count is equal to size of queue, it is full
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()