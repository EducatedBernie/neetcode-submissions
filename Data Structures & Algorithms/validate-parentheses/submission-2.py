class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        
        
        closing = ['}', ")", "]"] 
        opens = ["{", "[", "("]
        stk = []

        def getOpposite(s):
            if s == "{":
                return "}"
            if s== "(":
                return ")"
            if s == "[":
                return "]"
            return

        for brack in s:
            if brack in opens:
                stk.append(brack)

            elif brack in closing:
                if not stk:
                    return False
                top = stk.pop() # {
                if getOpposite(top) != brack:
                    print("top", top)
                    print("brack", brack)
                    return False
                else:
                    continue
        if stk:
            return False
        return True
                