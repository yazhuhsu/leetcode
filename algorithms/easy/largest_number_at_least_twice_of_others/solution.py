class Solution:
    def dominantIndex(self, nums: int) -> int:
        first, firstIdx, second = -1, -1, -1
        for idx, num in enumerate(nums):
            if first == -1:
                first, firstIdx = num, idx
                continue

            if num > first:
                second = first
                first, firstIdx = num, idx
                continue

            if num > second:
                second = num

        if first >= second * 2:
            return firstIdx

        return -1

solution = Solution()
print(solution.dominantIndex([3, 6, 1, 0]) == 1)
print(solution.dominantIndex([1, 2, 3, 4]) == -1)