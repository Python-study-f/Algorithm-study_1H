# https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.k = k
        self.dequeue = list()

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.dequeue) + 1 <= self.k:
            self.dequeue.insert(0, value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.dequeue) + 1 <= self.k:
            self.dequeue.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.dequeue):
            self.dequeue.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.dequeue):
            self.dequeue.pop()
            return True
        else:
            return False


    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not len(self.dequeue):
            return -1
        else:
            return self.dequeue[0]


    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not len(self.dequeue):
            return -1
        else:
            return self.dequeue[-1]


    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return not bool(len(self.dequeue))


    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.dequeue)==self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
