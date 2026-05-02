class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotateDict = {
            '0': '0',
            '1': '1',
            '2': '5',
            '5': '2',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        count = 0
        for i in range(0, n+1):
            origin, new = str(i), ''
            for s in str(i):
                if s not in rotateDict:
                    break
                
                new += rotateDict[s]

            if len(origin) == len(new) and origin != new:
                count += 1

        return count

solution = Solution()
print(solution.rotatedDigits(10) == 4)
print(solution.rotatedDigits(1) == 0)
print(solution.rotatedDigits(2) == 1)
print(solution.rotatedDigits(3) == 1)
print(solution.rotatedDigits(100) == 40)