class Solution:

    def encode(self, strs: List[str]) -> str:
        # puts a list of strings into a single string

        '''

        ["str", "str", "str", ] -> ["str/str/str"]
        '''

        # finding a delimintor that works. 

        lenMap = {}

        for s in strs:
            lenMap[s] = len(s) # {"neet": 4, "code": 4}

        res = ""

        for phrase, length in lenMap.items():
            res += str(length) + phrase # {4neet4code}

        return res
        

    def decode(self, s: str) -> List[str]:
        
        resList = []

        wordBegin = None

        i = 0
        while i < len(s): #while not at end of string
            toRead = int(s[i])
            print("toRead", toRead)
            wordBegin = i + 1
            while toRead > 0: #move the local index forward
                i+= 1
                toRead -= 1
            
            i += 1
            resList.append(s[wordBegin: i])
        return resList

            
        
         # parse the last couple of digits from lastIndex -> lastIndex + i
        # read a new number located at lastIndex
            
        

        