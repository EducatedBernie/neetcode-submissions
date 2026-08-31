class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['+', '-', '/', '*']

        stk = deque()

        ops = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: int(a / b),  # int() truncates toward zero
}

        # linear scan to populate respective stacks
        for num in tokens:
            if num in operands:

                right = int(stk.pop())

            
                left = int(stk.pop())

                stk.append(ops[num](left, right))
            else:
                stk.append(num)
        
        return int(stk[-1])
                


        

        