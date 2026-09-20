class MinStack:

    def __init__(self):
        self.topid = -1
        self.stack = []
        self.minnum = []
       
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.topid += 1

        if not self.minnum:
            self.minnum.append(val)
        else:
            new_min = min(val, self.minnum[-1])
            self.minnum.append(new_min)

    def pop(self) -> None:
        if self.topid != -1:
            self.stack.pop()
            self.minnum.pop()
            self.topid -= 1

    def top(self) -> int:
        if self.topid != -1:
            return self.stack[self.topid]
    
    def getMin(self) -> int:
        return self.minnum[self.topid]
        
