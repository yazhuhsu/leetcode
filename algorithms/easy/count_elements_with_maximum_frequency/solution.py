class Solution:
    def maxFrequencyElements(self, nums: list) -> int:
        frequencies, m = dict(), 0

        for n in nums:
            if n not in frequencies:
                frequencies[n] = 0

            frequencies[n] += 1

            if frequencies[n] > m:
                m = frequencies[n]

        count = 0
        for k, v in frequencies.items():
            if v == m:
                count += 1

        return count * m

print(Solution().maxFrequencyElements([1, 2, 2, 3, 1, 4]) == 4)
print(Solution().maxFrequencyElements([1, 2, 3, 4, 5]) == 5)