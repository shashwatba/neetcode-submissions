class MinStack:

    def __init__(self):
        self.stack = []
        self.minValue = None

    def push(self, val: int) -> None:
        if self.minValue == None or self.minValue > val:
            self.minValue = val
        self.stack.append([val, self.minValue])

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            a = self.stack[-1]
            self.minValue = a[1]
        else:
            self.minValue = None

    def top(self) -> int:
        a = self.stack[-1]
        return a[0]

    def getMin(self) -> int:
        a = self.stack[-1]
        return a[1]
        
