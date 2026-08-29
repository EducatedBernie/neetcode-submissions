class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        mx = 0

        l = 0
        r = len(heights) - 1
        
        while l < r:
            lh = heights[l]
            rh = heights[r]
            
            mx = max(((r - l)*min(lh, rh) ), mx)
            # print(lh, rh)
            
            if lh < rh:
                l += 1
                # print("left moves right")
            else:
                # (print("right moves left"))
                r -= 1

        return mx
        