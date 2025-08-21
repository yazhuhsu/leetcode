class Solution:
    def countSquares(self, matrix: list) -> int:
        max = len(matrix)
        if len(matrix[0]) < max:
            max = len(matrix[0])

        count = 0
        for side in range(0, max):
            for row in range(0, len(matrix)-side):
                for column in range(0, len(matrix[0])-side):
                    if side == 0:
                        if matrix[row][column] == 1:
                            count += 1
                    else:
                        filled = True
                        for hor in range(0, side+1):
                            for ver in range(0, side+1):
                                if matrix[row+hor][column+ver] == 0:
                                    filled = False
                                    break
                            if not filled:
                                break
                        if filled:
                            count += 1

        return count

cases = [
    [[1, 1],[1, 1]],
    [[0, 1, 1, 1],[1, 1, 1, 1],[0, 1, 1, 1]],
]

answers = [
    5, 15
]

solution = Solution()
for idx, v in enumerate(cases):
    answer = solution.countSquares(v)
    if answer != answers[idx]:
        print(f'n={v} Wrong!')
        print(f'output:{v}, answer:{answers}')
        break

    print(f'n={v} Correct!')