class Solution:

    def encode(self, strs: List[str]) -> str:

        enc = ""
        for s in strs:
            enc += str(len(s))
            enc += "$"
            enc += s

        print(enc)
        return enc

    def decode(self, s: str) -> List[str]:
        res = []

        index = 0
        while(index < len(s)):
            digit = ""
            while s[index] != "$":
                digit += (s[index]) 
                index += 1
            index += 1


            length = int(digit)
            word = ""
            while length > 0: # 3, 2, 1
                word += (s[index]) # 
                index += 1 # 2, 3, 4
                length -= 1 # 3, 2, 1, 

            res.append(word)

        return res
