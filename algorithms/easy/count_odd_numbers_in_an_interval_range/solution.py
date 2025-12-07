class Solution:
    def countOdds(self, low: int, high: int) -> int:
        num = 0
        if low % 2 == 1:
            num += 1
            low += 1
        if high % 2 == 1:
            num += 1
            high -=1

        num += int((high-low)/2)

        return num

solution = Solution()
print(solution.countOdds(3, 7) == 3)
print(solution.countOdds(8, 10) == 1)
print(solution.countOdds(0, 1000000000) == 500000000)
print(solution.countOdds(21, 22) == 1)