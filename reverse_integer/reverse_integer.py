class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        m = False
        min = -pow(2, 31)
        max = pow(2, 31)-1
        if x < 0:
            m = True
            x = -x
        
        while(x):
            if result*10 > min and result*10 < max:
                result *= 10
                result += int(x%10)
                x = int(x/10)
            else:
                return 0
        
        if m == True:
            result = -result
            
        return result
        