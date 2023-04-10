class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True

        prime_factors = [2, 3, 5]
        n_prime_factors = []
        for prime_factor in prime_factors:
            while n % prime_factor == 0:
                n_prime_factors.append(prime_factor)
                n = int(n / prime_factor)

        if n == 1:
            return True

        return False