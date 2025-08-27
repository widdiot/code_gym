from queue import Queue
class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        self.q.put(x)
        for i in range(self.q.qsize()-1):
            temp = self.q.get()
            self.q.put(temp)

    def pop(self) -> int:
        return self.q.get()

    def top(self) -> int:
        x = self.q.get()
        self.push(x)
        return x

    def empty(self) -> bool:
        return self.q.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()