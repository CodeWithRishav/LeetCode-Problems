from collections import deque

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = deque()
        self.prepareStack(nestedList)

    def next(self) -> int:
        if not self.hasNext():
            return None
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            lst = self.stack.pop().getList()
            self.prepareStack(lst)
        return bool(self.stack)

    def prepareStack(self, nestedList):
        for i in range(len(nestedList)-1, -1, -1):
            self.stack.append(nestedList[i])