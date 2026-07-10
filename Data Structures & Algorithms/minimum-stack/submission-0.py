class MinStack:
    stack: list[int]
    minStack: list[int]
    
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        prefixMin = val
        if len(self.minStack) >= 1:
            prefixMin = self.getMin()
        self.minStack.append(min(val, prefixMin))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
