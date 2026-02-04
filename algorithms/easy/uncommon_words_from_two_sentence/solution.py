class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list:
        words1, words2 = s1.split(), s2.split()
        word_dict = dict()
        for _, word in enumerate(words1 + words2):
            if word not in word_dict:
                word_dict[word] = 0
            word_dict[word] += 1

        uncommon_words = []
        for k, v in word_dict.items():
            if v == 1:
                uncommon_words.append(k)

        return uncommon_words

solution = Solution()
print(solution.uncommonFromSentences("apple apple", "banana") == ["banana"])
print(solution.uncommonFromSentences("this apple is sweet", "this apple is sour") == ["sweet", "sour"])