class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    # two pointer approach for sorted two sum is n 

    # sorting takes n log n + n

    # sort, perserve indices # how to do? use enumerate
    # how to use sorted and sort? 
    # 
        nums = sorted(nums)

        # -4, -1, -1, 0, 1, 2
        #  

        res = []

        for i in range(len(nums) - 2):

            if nums[i] == nums[i-1] and i-1 != 0:
                continue
            # i = fixed
            subTarget = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1

        
            while j < k:
                if nums[j] + nums[k] > subTarget:
                    k -= 1
                    if nums[k] == nums[k+1] and k+1 < len(nums):
                        continue
                    
                elif nums[j] + nums[k] < subTarget:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    
                    

        return res
     
