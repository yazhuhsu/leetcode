class Solution:
    def minBitwiseArray(self, nums: list) -> list:
        answers = []
        for idx, num in enumerate(nums):
            for i in range(1, num+1):
                if (i | (i+1)) == num:
                    answers.append(i)
                    break
            
            if len(answers) != idx+1:
                answers.append(-1)

        return answers

solution = Solution()
print(solution.minBitwiseArray([2, 3, 5, 7]) == [-1, 1, 4, 3])
print(solution.minBitwiseArray([11, 13, 31]) == [9, 12, 15])
print(solution.minBitwiseArray([149, 521, 71, 967, 449, 101, 439, 557, 73, 179]) == [148, 520, 67, 963, 448, 100, 435, 556, 72, 177])