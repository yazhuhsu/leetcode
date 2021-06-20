class Solution:
    """
    lengthOfLastWord

    given a string `s` consists of some words seperated by spaces,
    if last word exists: return the length of last word
    if last word not exists: return 0
    """
    def lengthOfLastWord(self, s: str) -> int:
        
        words = list()
        # clean up for empty string
        for word in s.split(" "):
            if word != '':
                words.append(word)
                
        word_length = len(words)
        if word_length > 0:
            return len(words[word_length-1])
        else:
            return 0