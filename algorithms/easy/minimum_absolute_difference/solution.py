class Solution:
    def minimumAbsDifference(self, arr: list) -> list:
        arr.sort()

        mini, differences = -1, []
        for i in range(len(arr)-1):
            abs_diff = arr[i+1]-arr[i]
            if mini == -1 or abs_diff < mini:
                mini = abs_diff

        for i in range(len(arr)-1):
            abs_diff = arr[i+1]-arr[i]
            if abs_diff == mini:
                differences.append([arr[i], arr[i+1]])

        return differences

solution = Solution()
print(solution.minimumAbsDifference([4, 2, 1, 3]) == [[1, 2], [2, 3], [3, 4]])
print(solution.minimumAbsDifference([1, 3, 6, 10, 15]) == [[1, 3]])
print(solution.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]) == [[-14, -10], [19, 23], [23, 27]])