class Solution:
    def longestSubarray(self, nums: list) -> int:
        zeros = []
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zeros.append(i)

        if len(zeros) == 0:
            return len(nums)-1

        max = 0
        for z in range(0, len(zeros)):
            start, end = 0, len(nums)-1
            if z != 0:
                start = zeros[z-1]+1
            if z != len(zeros)-1:
                end = zeros[z+1]-1

            if end-start > max:
                max=end-start

        return max

cases = [
    [1,1,0,1],
    [0,1,1,1,0,1,1,0,1],
    [1,1,1]
]

answers = [3,5,2]

solution = Solution()
for idx, v in enumerate(cases):
    answer = solution.longestSubarray(v)
    if answer != answers[idx]:
        print(f'n={v} Wrong!')
        print(f'output:{v}, answer:{answers}')
        break
    
    print(f'n={v} Correct!')