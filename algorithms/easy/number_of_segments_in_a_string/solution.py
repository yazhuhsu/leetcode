class Solution:
    def countSegments(self, s: str) -> int:
        word, words = '', []
        for sub in s:
            if sub == ' ':
                if word != '':
                    words.append(word)
                    word=''
                continue

            word += sub

        if word != '':
            words.append(word)
            
        return len(words)


print(Solution().countSegments("Hello, my name is John") == 5)
print(Solution().countSegments("Hello") == 1)