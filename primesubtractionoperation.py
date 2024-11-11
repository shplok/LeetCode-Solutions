from typing import List

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False 
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    # Collect all prime numbers less than the limit
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

def largest_prime_below(n):
    primes = sieve_of_eratosthenes(n - 1)
    return primes[-1] if primes else None  # Get the largest prime less than n

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Generate primes up to a reasonable upper bound once
        max_val = max(nums)
        primes = sieve_of_eratosthenes(max_val)

        prev = 0
        for i in range(len(nums)):
            max_prime = None
            for prime in primes:
                if prime < nums[i] and (i == 0 or nums[i] - prime > prev):
                    max_prime = prime
                else:
                    break
            
            if max_prime is not None:
                nums[i] -= max_prime
            
            if nums[i] <= prev:  # Check if the list remains sorted in increasing order
                return False
            prev = nums[i]
        
        return True
