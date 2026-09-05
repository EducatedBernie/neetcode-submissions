class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
      # left 
      # right 
      # maxLen 
      # freqMap
      # maxElement = 'A'

      # for r in len
      #      while m + k < length of substring

      #      shrink the window 
            # calculate
        freqMap = defaultdict(int)
        left = 0
        maxLen = 0
        for right in range(len(s)):
            freqMap[s[right]] += 1
            m = max(freqMap.values())
            while m + k < right - left + 1:
                freqMap[s[left]] -= 1
                m = max(freqMap.values())
                left += 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen