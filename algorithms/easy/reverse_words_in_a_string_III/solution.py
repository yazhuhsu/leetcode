class Solution:
    def reverseWords(self, s: str) -> str:
        output = ''
        words = s.split(' ')

        for idx, word in enumerate(words):
            for widx in range(len(word)):
                output += word[len(word)-widx-1]
            if idx < len(words)-1:
                output += ' '

        return output

solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest")=="s'teL ekat edoCteeL tsetnoc")
print(solution.reverseWords("Mr Ding")=="rM gniD")