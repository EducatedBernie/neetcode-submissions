class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # how many days in the future does it take
        # to get a WARMER day than today

        stk = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stk and temp > stk[-1][1]:
                dayIdx, dayTemp = stk.pop()
                res[dayIdx] = idx - dayIdx
            stk.append((idx, temp))

        return res
                # compute how many days passed and also update the result

                
                
                

