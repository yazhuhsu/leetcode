# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return n

        min_n, max_n = 1, n+1
        picked = int((min_n+max_n)/2)
        direction = guess(picked)
        while direction != 0:
            if direction == 1:
                min_n = picked
            else:
                max_n = picked
            
            picked = int((min_n+max_n)/2)
            direction = guess(picked)
        
        return picked