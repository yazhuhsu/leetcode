import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        replacer = {
            ",": " ",
            "!": " ",
            "?": " ",
            "'": " ",
            ";": " ",
            ".": " "
        }

        pattern = re.compile("|".join(re.escape(key) for key in replacer.keys()))
        sentence = pattern.sub(lambda match: replacer[match.group(0)], paragraph)

        words = sentence.split(" ")
        word_dict, banned_dict = {}, {}
        for _, word in enumerate(words):
            if word == "":
                continue
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

            word_dict[word.lower()] += 1

        for _, word in enumerate(banned):
            if word not in banned_dict:
                banned_dict[word] = True

        max_count, max_word = 0, ""
        for word, count in word_dict.items():
            if count > max_count and word not in banned_dict:
                max_count = count
                max_word = word

        return max_word

solution = Solution()
print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]) == "ball")
print(solution.mostCommonWord("a.", []) == "a")
print(solution.mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]) == "ball")