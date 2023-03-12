class Solution:
    def isPalindrome(self, s: str) -> bool:
        origin = ''
        reversed = ''
        for a in s:
            if a.isalpha() or a.isnumeric():
                origin += a
                reversed = a + reversed

        if origin.lower() == reversed.lower():
            return True
        
        return False