class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1,  1,  2, 3, 5, 

        # Compute the inverse? 

        for i in range(len(numbers)):
            diff = target - numbers[i]
            try:
                targetIndex = numbers.index(diff)
            except ValueError:
                continue
 
            if targetIndex != -1:
                return [i+1, targetIndex+1]
