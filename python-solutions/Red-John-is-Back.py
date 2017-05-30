import sys

def gen_primes_lt(n):
    primes_sieve = range(n+1)
    primes_sieve[1] = 0
    for i in xrange(2, int(round(n**0.5))+1):
        if primes_sieve[i]:
            primes_sieve[i*i: n+1: i] = [0] * len(xrange(i*i, n+1, i))
    return filter(None, primes_sieve)

def gen_tilings(n):
    result = [1, 1, 1, 1, 2]
    for i in range(5,n+1):
        result.append(result[i-1] + result[i-4])
    return result

t = int(raw_input())
n = [int(raw_input()) for x in range(0, t)]

tilings = gen_tilings(max(n))
primes_lt_list = gen_primes_lt(max(tilings))

for x in n:
    print len(gen_primes_lt(tilings[x]))
