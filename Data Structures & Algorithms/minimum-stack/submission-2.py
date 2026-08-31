class MinStack:

    def __init__(self):
        self.stk = []
        self.mini = float("inf")
        self.minstk = []

    def push(self, val: int) -> None:
        # check if minimum
        if val <= self.mini:
            self.minstk.append(val)
            self.mini = val

        self.stk.append(val)
        

    def pop(self) -> None:
        outgoingElement = self.stk.pop()
        if outgoingElement == self.mini:
            self.minstk.pop()
            if self.minstk:
                self.mini = self.minstk[-1]
            else:
                self.mini = float("inf")

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.mini

    # 20
    # 20
