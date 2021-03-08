# 28 ms	14.2 MB
# https://leetcode.com/problems/implement-queue-using-stacks/submissions/
class MyQueue:
    stack = None
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tmp = self.stack[0]
        del self.stack[0]
        return tmp
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]
    
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.stack:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()