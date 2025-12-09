class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 0 or n == 1:
            return True

        first, second, third = -1, -1, -1
        while n >= 1:
            first, second = second, third
            if n % 2 == 1:
                third = 1
            else:
                third = 0

            n = int(n/2)

            if first == -1 or second == -1 or third == -1:
                continue
            if (first+second) % 2 == 0 or (second+third) % 2 == 0:
                return False


        if (first+second) % 2 == 0 or (second+third) % 2 == 0:
            return False

        return True

solution = Solution()
print(solution.hasAlternatingBits(5)==True)
print(solution.hasAlternatingBits(7)==False)
print(solution.hasAlternatingBits(11)==False)