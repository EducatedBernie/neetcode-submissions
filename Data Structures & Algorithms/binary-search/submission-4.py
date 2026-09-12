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

        if lo not in range(len(nums)) or nums[lo] != target:
            return -1
        else:
            return lo
        
        def check(idx):
            return nums[idx] >= target

        
        