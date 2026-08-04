class Solution:

    def encode(self, strs: List[str]) -> str:
        # puts a list of strings into a single string

        '''

        ["str", "str", "str", ] -> ["str/str/str"]
        '''

        # finding a delimintor that works. 

        concat = "DELIMETER".join(strs)

        return concat

    def decode(self, s: str) -> List[str]:

        return s.split("DELIMETER")

        # puts a single string into a list of strings