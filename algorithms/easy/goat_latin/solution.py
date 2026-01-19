class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        words = sentence.split(" ")

        final_sentence = ""
        for idx, word in enumerate(words):
            if word[0] in vowels:
                final_sentence += word + "ma"
            else:
                final_sentence += word[1:] + word[0] + "ma"

            for _ in range(idx+1):
                final_sentence += "a"

            if idx != len(words)-1:
                final_sentence += " "

        return final_sentence

solution = Solution()
print(solution.toGoatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
print(solution.toGoatLatin("The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")