class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        winLen = len(s1)
        left = 0
        freqMap = defaultdict(int)
        signature = collections.Counter(s1) # 

        
        for i in range(left, winLen - 1):
            freqMap[s2[i]] += 1
        for right in range(winLen - 1, len(s2)):
            freqMap[s2[right]] += 1
            # check 
            print(signature)
            print(freqMap)
            print(right)
            if signature == freqMap:
                return True
            # shift window right side
            
            freqMap[s2[left]] -= 1 
            if freqMap[s2[left]] == 0:
                del freqMap[s2[left]]   
            left += 1
        return False
            
        # del dict[key]
            
            

