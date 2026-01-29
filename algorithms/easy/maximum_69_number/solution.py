class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str, max_num = str(num), num
        for i in range(len(num_str)):
            if num_str[i] == '6':
                count = num + 3 * (10**(len(num_str)-i-1))
                if count > max_num:
                    max_num = count

        return max_num

solution = Solution()
print(solution.maximum69Number(9669) == 9969)
print(solution.maximum69Number(9996) == 9999)
print(solution.maximum69Number(9999) == 9999)