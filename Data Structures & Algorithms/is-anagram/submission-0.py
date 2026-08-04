class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # understand:
        
        # create a frequency map after iter through string1
        # create a freq map after iter through string2
        # compare the freq

        ctr1 = collections.Counter(s)
        ctr2 = collections.Counter(t)

        for letter, freq in ctr1.items():
            if freq != ctr2[letter]:
                return False
        
        return True