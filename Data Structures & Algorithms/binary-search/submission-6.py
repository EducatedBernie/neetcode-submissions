class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        def check(idx):
            return nums[idx] >= target 

        while lo <= hi:
            mid = lo + (hi - lo) // 2 
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        if lo < len(nums) and nums[lo] == target:
            return lo
        else:
            return -1
        
        def check(idx):
            return nums[idx] >= target

        
        