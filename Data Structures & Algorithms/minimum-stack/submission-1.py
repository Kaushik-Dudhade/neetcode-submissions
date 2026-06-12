class MinStack:

    def __init__(self):
        self.stack = []
        self.stackMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stackMin.append(min(val, (self.stackMin[-1]) if self.stackMin else float('inf')))

    def pop(self) -> None:
        self.stack.pop()
        self.stackMin.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1
        

    def getMin(self) -> int:
        return self.stackMin[-1]
        
