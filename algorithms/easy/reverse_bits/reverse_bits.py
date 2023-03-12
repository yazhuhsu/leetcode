class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        while n != 0:
            bit = n % 2
            bits.append(bit)
            n //= 2

        while len(bits) < 32:
            bits.append(0)
        
        bits.reverse()

        output = 0
        for idx, bit in enumerate(bits):
            output += bit * (2 ** idx)

        return output