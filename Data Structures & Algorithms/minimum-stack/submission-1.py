class MinStack:

    def __init__(self):
        self.stack = []
        self.minnum = []
       
    
    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minnum:
            self.minnum.append(val)
        else:
            new_min = min(val, self.minnum[-1])
            self.minnum.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minnum.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minnum[-1]
        
