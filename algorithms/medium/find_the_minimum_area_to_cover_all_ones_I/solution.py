class Solution:
    def minimumArea(self, grid: list) -> int:

        top, down, left, right = -1, -1, -1, -1
        for row in range(0, len(grid)):
            for column in range(0, len(grid[0])):
                if top == -1 and grid[row][column] == 1:
                    top = row
                if down == -1 and grid[len(grid)-row-1][len(grid[0])-column-1] == 1:
                    down = len(grid)-row-1
        
        for column in range(0, len(grid[0])):
            for row in range(0, len(grid)):
                if left == -1 and grid[row][column] == 1:
                    left = column
                if right == -1 and grid[len(grid)-row-1][len(grid[0])-column-1] == 1:
                    right = len(grid[0])-column-1
        

        w, h = right-left+1, down-top+1

        return w*h

cases = [
    [[0,1,0],[1,0,1]],
    [[1,0],[0,0]]
]

answers = [6, 1]

solution = Solution()
for idx, v in enumerate(cases):
    answer = solution.minimumArea(v)
    if answer != answers[idx]:
        print(f'n={v} Wrong!')
        print(f'output:{v}, answer:{answers}')
        break

    print(f'n={v} Correct!')