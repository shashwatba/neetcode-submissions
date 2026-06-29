class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 9999999999999
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        a = self.stack.pop()
        if a == self.min:
            newMin = 9999999999
            for num in self.stack:
                if num < newMin:
                    newMin = num

            self.min = newMin

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        
