class Solution:
    def maximumHappinessSum(self, happiness: list, k: int) -> int:
        happiness.sort(reverse=True)

        max_sum = 0
        for idx, value in enumerate(happiness[:k]):
            if value-idx < 0:
                break
            max_sum += value-idx

        return max_sum

solution = Solution()
print(solution.maximumHappinessSum([1, 2, 3], 2) == 4)
print(solution.maximumHappinessSum([1, 1, 1, 1], 2) == 1)
print(solution.maximumHappinessSum([2, 3, 4, 5], 1) == 5)