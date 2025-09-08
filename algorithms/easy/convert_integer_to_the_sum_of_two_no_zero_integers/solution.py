class Solution:
    def getNoZeroIntegers(self, n: int) -> list:
        outputs = []
        for i in range(1, n+1):
            if '0' in str(i) or '0' in str(n-i):
                continue

            outputs.append(i)
            outputs.append(n-i)
            break

        return outputs

cases = [
    2, 11
]

answers = [
    [1, 1],
    [2, 9],
]

solution = Solution()
for idx, v in enumerate(cases):
    answer = solution.getNoZeroIntegers(v)
    if answer != answers[idx]:
        print(f'n={v} Wrong!')
        print(f'output:{v}, answer:{answers}')
        break

    print(f'n={v} Correct!')