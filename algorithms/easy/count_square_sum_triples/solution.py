class Solution:
    def countTriples(self, n: int) -> int:
        triples = dict()
        for i in range(n, 0, -1):
            for j in range(i-1, 0, -1):
                k = (i*i-j*j)**0.5
                if int(k.real) == k and int(k.real) < i and (j,int(k.real),i) not in triples:
                    triples[(j,int(k.real),i)] = True
                    
        return len(triples)

solution = Solution()
print(solution.countTriples(5)==2)
print(solution.countTriples(10)==4)