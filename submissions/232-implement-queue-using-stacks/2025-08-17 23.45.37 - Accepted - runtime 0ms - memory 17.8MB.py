class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        for i in range(len(self.s1)-1):
            x = self.s1.pop()
            self.s2.append(x)
        res = self.s1.pop()
        for i in range(len(self.s2)):
            x = self.s2.pop()
            self.s1.append(x)
        return res


    def peek(self) -> int:
        return self.s1[0]

    def empty(self) -> bool:
        return not len(self.s1)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()