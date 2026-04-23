class MinStack:
    def __init__(self):      
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)
        

    def top(self) -> int:
        val = self.stack[-1]
        return val
        

    def getMin(self) -> int:
        minimum = float("inf")
        for i in range(len(self.stack)):
            minimum = min(minimum, self.stack[i])
        return minimum
