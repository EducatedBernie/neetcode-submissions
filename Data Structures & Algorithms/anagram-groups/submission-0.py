class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force solution sort all the anagrams and then try to match them 

        # n (n log n)

        # go through list once

        # put all length 3 anagrams to one list
        # put all length 4 anagrams to another
        # put all length 5

        res = []

        lengthSets = defaultdict(list)

        for word in strs:
            lengthSets[len(word)].append(word)

        

        def groupSameLenAnagrams(arr):
            lookUp = defaultdict(list)
            
            for word in arr:
                unicode = 0
                for char in word:
                    unicode += (ord(char) - ord('a'))
                lookUp[unicode].append(word)
            return lookUp.values()
        

        for length, lenSet in lengthSets.items():
            for individualSet in groupSameLenAnagrams(lenSet):
                res.append(individualSet)

        return res
            
            
            