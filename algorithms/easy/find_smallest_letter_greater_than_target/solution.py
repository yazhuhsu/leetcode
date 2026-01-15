class Solution:
    def nextGreatestLetter(self, letters: list, target: str) -> str:
        for _, letter in enumerate(letters):
            if letter > target:
                return letter

        return letters[0]

solution = Solution()
print(solution.nextGreatestLetter(["c", "f", "j"], "a") == "c")
print(solution.nextGreatestLetter(["c", "f", "j"], "c") == "f")