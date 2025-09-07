class Solution:
    def sumZero(self, n: int) -> list:
        outputs = []
        if n%2 == 1:
            n -= 1
            outputs.append(0)

        for i in range(2, n+2):
            output = int(i/2)
            if i % 2 == 1:
                output = -output
            outputs.append(output)

        return outputs

cases = [
    5, 3, 1
]

answers = [
    [0, 1, -1, 2, -2],
    [0, 1, -1],
    [0]
]

solution = Solution()
for idx, v in enumerate(cases):
    answer = solution.sumZero(v)
    if answer != answers[idx]:
        print(f'n={v} Wrong!')
        print(f'output:{v}, answer:{answers}')
        break

    print(f'n={v} Correct!')