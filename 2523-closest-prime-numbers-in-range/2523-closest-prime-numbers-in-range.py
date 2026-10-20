class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        sieve = [True] * (right + 1)

        sieve[0] = sieve[1] = False

        def mark_non_primes(start, step):
            for j in range(start, len(sieve), step):
                sieve[j] = False
            
        for i in range(2, int(sqrt(len(sieve)) + 1)):
            if sieve[i]:
                mark_non_primes(i * i, i)
        
        l = left
        r = left + 1

        res = [-1, -1]
        min_gap = float('inf')

        while r <= right:
            if sieve[l] and sieve[r]:
                if r - l < min_gap:
                    res = [l, r]
                    min_gap = r - l
                l = r
                r += 1
            elif sieve[l] and not sieve[r]:
                r += 1
            elif not sieve[l] and sieve[r]:
                l = r
                r += 1
            else:
                l += 1
                r += 1
        return res





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna