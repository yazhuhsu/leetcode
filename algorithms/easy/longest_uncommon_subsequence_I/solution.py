class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        first, second = self.find(a, b), self.find(b, a)
        if second > first:
            return second

        return first
        
    def find(self, a: str, b: str) -> int:
        matches = []
        for i in range(0, len(b)):
            if i+len(a) > len(b):
                break

            if b[i:i+len(a)] == a:
                matches.append(i)
                matches.append(i+len(a))

        if len(matches) == 0:
            return len(a)

        return -1

solution = Solution()
print(solution.findLUSlength("aba", "cdc") == 3)
print(solution.findLUSlength("aaa", "aaa") == -1)
print(solution.findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef") == 17)
print(solution.findLUSlength("aefeaf", "a") == 6)
print(solution.findLUSlength("abab", "cdc") == 4)