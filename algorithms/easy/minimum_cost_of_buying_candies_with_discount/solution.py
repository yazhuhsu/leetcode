class Solution:
    def minimumCost(self, cost: list) -> int:
        cost.sort(reverse=True)

        costs, bought = 0, 0
        for _, c in enumerate(cost):
            if bought == 2:
                bought = 0
                continue
            costs += c
            bought += 1

        return costs

solution = Solution()
print(solution.minimumCost([1, 2, 3]) == 5)
print(solution.minimumCost([6, 5, 7, 9, 2, 2]) == 23)
print(solution.minimumCost([5, 5]) == 10)
print(solution.minimumCost([1]) == 1)
print(solution.minimumCost([3, 3, 3]) == 6)