class MyQueue:

    def __init__(self):
        self.sk = []
        self.rsk = []

    def push(self, x: int) -> None:
        self.sk.append(x);
        

    def pop(self) -> int:
        self.peek()
        return self.rsk.pop()

    def peek(self) -> int:
        if self.rsk:
            return self.rsk[-1]
        else:
            while self.sk:
                self.rsk.append(self.sk.pop())
            return self.rsk[-1]
        

    def empty(self) -> bool:
        
        return not (self.sk or self.rsk)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()