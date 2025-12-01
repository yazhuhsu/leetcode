class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first, upper, lower = 0, 0, 0
        for idx, w in enumerate(word):
            if w.isupper():
                upper += 1
                if idx == 0:
                    first += 1
            else:
                lower += 1

        if first == 1 and upper == 1:
            return True
        if upper == len(word) or lower == len(word):
            return True

        return False

solution = Solution()
print(solution.detectCapitalUse("USA")==True)
print(solution.detectCapitalUse("FlaG")==False)