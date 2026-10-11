# LeetCode Problem Number - 204

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        is_prime = [True] * n            # indices 0..n-1
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:              # i is prime -> cross out its multiples
                is_prime[i * i:n:i] = [False] * len(range(i * i, n, i))
        return sum(is_prime)             # True == 1, so the sum is the count

