class Solution:
    def countNegatives(self, grid: list) -> int:
        count = 0
        for i in range(0, len(grid)):
            for j in range(len(grid[0])-1, -1, -1):
                if grid[i][j] >= 0:
                    break

                count += 1

        return count

solution = Solution()
print(solution.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]) == 8)
print(solution.countNegatives([[3, 2], [1, 0]]) == 0)