class Solution:
    def findWords(self, words: list) -> list:
        rows = {
            1: ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            2: ["a", "s", "d", "f", "g", "h", "j", "k", "l", "A", "S", "D", "F", "G", "H", "J", "K", "L"],
            3: ["z", "x", "c", "v", "b", "n", "m", "Z", "X", "C", "V", "B", "N", "M"]
        }

        outputs = []
        for word in words:
            row1, row2, row3 = 0, 0, 0
            for w in word:
                if w in rows[1]:
                    row1 += 1
                elif w in rows[2]:
                    row2 += 1
                elif w in rows[3]:
                    row3 += 1

            if row1 == len(word) or row2 == len(word) or row3 == len(word):
                outputs.append(word)

        return outputs

solution = Solution()
print(solution.findWords(["Hello", "Alaska", "Dad", "Peace"])== ["Alaska", "Dad"])
print(solution.findWords(["omk"]) == [])
print(solution.findWords(["adsdf", "sfd"]) == ["adsdf", "sfd"])