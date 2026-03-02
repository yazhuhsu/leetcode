import math

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime = 0
        for i in range(0, right-left+1):
            num, bits = left+i, 0
            while num > 0:
                bits += int(num % 2)
                num /= 2

            if self.isPrime(bits):
                prime += 1

        return prime
        
    def isPrime(self, num) -> bool:
        if num < 2:
            return False

        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        
        return True

solution = Solution()
print(solution.countPrimeSetBits(6, 10) == 4)
print(solution.countPrimeSetBits(10, 15) == 5)