class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = []
        while n != 0:
            bit = n % 2
            bits.append(bit)
            n //= 2

        count = 0
        for bit in bits:
            if bit == 1:
                count += 1

        return count