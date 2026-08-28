class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # array is sorted so we can converge in the middle
        

        # return the indices

        i = 0
        j = len(numbers) - 1
        while i < j: 
            # check at each step
            if numbers[i] + numbers[j] > target:
                j -= 1
                
            elif numbers[i] + numbers[j] < target:
                i += 1
                
            elif numbers[i] + numbers[j] == target:
                break
        
        return [i+1, j+1]
            


            # if the two indices if add up to target
            
            