class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

solution = Solution()
print(solution.toLowerCase("Hello") == "hello")
print(solution.toLowerCase("here") == "here")
print(solution.toLowerCase("LOVELY") == "lovely")