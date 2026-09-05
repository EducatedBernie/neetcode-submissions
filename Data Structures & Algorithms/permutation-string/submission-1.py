class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # initialize signature and counter


        # our right pointer goes from s1 + 1 to len(s1) - 1
            # 

            # learnings, don't do weird initializations
            # learnings, comparing the "signature" and the defaultdict, there's an problem where A:0, B:1 where as signatuer is just B:1, these two dictionaries are NOT equal, even tho they are essentially equal. 

            signature = collections.Counter(s1)
            freqMap = defaultdict(int)
            left = 0
            for right in range(len(s2)):
            

                freqMap[s2[right]] += 1
                
                if right > len(s1) - 1:
                    freqMap[s2[left]] -= 1
                    if freqMap[s2[left]] == 0:
                        del freqMap[s2[left]]
                    left += 1
                if freqMap == signature:
                    return True

                

            return False