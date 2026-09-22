class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1 or len(s) ==0:
            return len(s)

        left = 0
        right = 0
        chars = set()
        maxLen = 0

        chars.add(s[0])

        while right < len(s) - 1: #0 < 1
            right += 1 #1
            while s[right] in chars: 
                # shrink left 
                # print(s[left])
                chars.remove(s[left]) #"a removed"
                left += 1 #left on 1
            chars.add(s[right]) #a added
            # print(s[right])
            maxLen = max(maxLen, right - left + 1)
        return maxLen       