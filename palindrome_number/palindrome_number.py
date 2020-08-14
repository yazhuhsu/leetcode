class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        result = 0
        original = x
        
        while x > 0:
            result *= 10
            result += int(x%10)
            x = int(x/10)
            
        if result == original:
            return True
        
        return False
        