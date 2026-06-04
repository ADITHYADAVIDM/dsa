class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_val = val
            self.stack.append((val, self.min_val))
        else:
            if self.min_val > val:
                self.min_val = val
                self.stack.append((val, self.min_val))
            else:
                self.stack.append((val, self.min_val))
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            if not self.stack:
                self.min_val = float('inf')
            else:
                self.min_val = self.stack[-1][1]


    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]

example = MinStack()
example.push(-2)
example.push(0)
example.push(-3)
print(example.getMin())
example.pop()
print(example.top())
print(example.getMin())