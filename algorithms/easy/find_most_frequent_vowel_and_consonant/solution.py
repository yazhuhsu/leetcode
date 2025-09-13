class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = {'a':0,'e':0,'i':0,'o':0,'u':0}
        other = {}
        for v in s:
            if v in ['a','e','i','o','u']:
                freq[v] += 1
                continue
            if v not in other:
                other[v] = 0
            other[v]+=1

        m = 0
        if len(freq) != 0:
            m += max(freq.values())
        if len(other) != 0:
            m += max(other.values())

        return m

cases =  {
    'successes': 6,
    'aeiaeia': 3,
}

solution = Solution()
for k, v in cases.items():
    answer = solution.maxFreqSum(k)
    if answer != v:
        print(f'n={v} Wrong!')
        print(f'output:{v}, answer:{v}')
        break

    print(f'n={v} Correct!')