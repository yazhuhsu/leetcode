class Solution:
    def areaOfMaxDiagonal(self, dimensions: list) -> int:
        maximum, width, height = 0, 0, 0
        for i in range(0,len(dimensions)):
            w, h = dimensions[i][0], dimensions[i][1]
            if w*w+h*h > maximum:
                maximum = w*w+h*h
                width, height = w, h
            elif w*w+h*h == maximum and w*h > width*height:
                maximum = w*w+h*h
                width, height = w, h
        
        return width*height

cases = [
    [[9,3],[8,6]],
    [[3,4],[4,3]]
]

answers = [48, 12]

solution = Solution()
for idx, v in enumerate(cases):
    answer = solution.areaOfMaxDiagonal(v)
    if answer != answers[idx]:
        print(f'n={v} Wrong!')
        print(f'output:{v}, answer:{answers}')
        break

    print(f'n={v} Correct!')