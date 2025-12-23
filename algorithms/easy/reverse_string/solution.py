class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)/2
        if length % 2 == 1:
            length = (len(s)+1)/2

        for i in range(int(length)):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]

        return

solution = Solution()
s = ["h", "e", "l", "l", "o"]
solution.reverseString(s)
print(s == ["o", "l", "l", "e", "h"])

s = ["H", "a", "n", "n", "a", "h"]
solution.reverseString(s)
print(s == ["h", "a", "n", "n", "a", "H"])