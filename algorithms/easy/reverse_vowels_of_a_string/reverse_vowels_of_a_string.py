# refers to: #345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/

# Given an string `s`, reverse only all the vowels in the string and return it.
# The vowels are `a`, `e`, `i`, `o`, `u` in both lower and upper case.
# Example:
# s="hello" --> "holle"
# s="leetcode" --> "leotcede" 

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for idx, c in enumerate(s):
            if c in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
                vowels.append(c)

        vowel_idx, vowels = 0, vowels[::-1]
        reversed_s = ""
        for idx, c in enumerate(s):
            if c in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
                reversed_s += vowels[vowel_idx]
                vowel_idx += 1
            else:
                reversed_s += c

        return reversed_s