class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alpha = ""
        for idx, ch in enumerate(s):
            if ch.isalpha():
                alpha += ch

        idx, reverse = 0, ""
        for _, ch in enumerate(s):
            if ch.isalpha():
                reverse += alpha[len(alpha)-idx-1]
                idx += 1
                continue
            
            reverse += ch

        return reverse

solution = Solution()
print(solution.reverseOnlyLetters("ab-cd") == "dc-ba")
print(solution.reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba")
print(solution.reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!")