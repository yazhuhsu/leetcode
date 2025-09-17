class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')

        count = 0
        exist = False
        for word in words:
            for letter in word:
                for broken in brokenLetters:
                    if letter == broken:
                        count += 1
                        exist = True
                        break
                if exist:
                    break
            exist = False

        return len(words)-count

cases = [
    ('hello world', 'ad', 1),
    ('leet code', 'lt', 1),
    ('leetcode', 'e', 0)
]

solution = Solution()
for idx, v in enumerate(cases):
    answer = solution.canBeTypedWords(v[0], v[1])
    if answer != v[2]:
        print(f'n={v} Wrong!')
        print(f'output:{v}, answer:{v[2]}')
        break

    print(f'n={v} Correct!')