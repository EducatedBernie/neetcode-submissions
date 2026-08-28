class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two poitner method converging into the middle
        

        cleaned = "".join(char for char in s if char.isalnum())

        i = 0
        j = len(cleaned) - 1

        while i < j: 
            #
            if cleaned[i].lower() == cleaned[j].lower():
            # loop incr
                i += 1
                j -= 1
            else:
                return False

        return True

        


            

        