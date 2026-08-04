class Solution:

    def encode(self, strs: List[str]) -> str:
        # puts a list of strings into a single string

        '''

        ["str", "str", "str", ] -> ["str/str/str"]
        '''

        # finding a delimintor that works. 

        if strs == [""]:
            return []

        concat = "DELIMETER".join(strs)

        return concat

    def decode(self, s: str) -> List[str]:

        if s == []:
            return [""]
        return s.split("DELIMETER")

        # puts a single string into a list of strings