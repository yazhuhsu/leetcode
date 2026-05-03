class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for _ in range(len(s)):
            if s[1:]+s[0] == goal:
                return True

            s = s[1:]+s[0]

        return False

solution = Solution()
print(solution.rotateString("abcde", "cdeab") == True)
print(solution.rotateString("abcde", "abced") == False)
print(solution.rotateString("abcde", "abcde") == True)
print(solution.rotateString("a", "a") == True)
print(solution.rotateString("aa", "aa") == True)