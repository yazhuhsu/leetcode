class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_letters = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }

        if digits == "":
            return []
        if len(digits) == 1:
            return digits_to_letters[int(digits)]

        letters = []
        combinations = []
        for digit in digits:
            letters.append(digits_to_letters[int(digit)])

        if len(letters) == 2:
            for i in letters[0]:
                for j in letters[1]:
                    combinations.append(f"{i}{j}")
        
        if len(letters) == 3:
            for i in letters[0]:
                for j in letters[1]:
                    for k in letters[2]:
                        combinations.append(f"{i}{j}{k}")
        
        if len(letters) == 4:
            for i in letters[0]:
                for j in letters[1]:
                    for k in letters[2]:
                        for l in letters[3]:
                            combinations.append(f"{i}{j}{k}{l}")
        
        return combinations