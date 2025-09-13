class Solution:
    def sortVowels(self, s: str) -> str:
        if len(s) == 1:
            return s

        vowels = []
        for v in s:
            if v in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vowels.append(v)
        
        if len(vowels) == len(s):
            return ''.join(sorted(vowels))

        vowels.sort()

        output, idx = '', 0
        for v in s:
            if v in vowels:
                output += vowels[idx]
                idx += 1
                continue
            output += v

        return output

cases = [
    'lEetcOde', 'lYmpH', 'u', 'OA'
]

answers = [
    'lEOtcede', 'lYmpH', 'u', 'AO'
]

solution = Solution()
for idx, v in enumerate(cases):
    answer = solution.sortVowels(v)
    if answer != answers[idx]:
        print(f'n={v} Wrong!')
        print(f'output:{v}, answer:{answers}')
        break
    
    print(f'n={v} Correct!')