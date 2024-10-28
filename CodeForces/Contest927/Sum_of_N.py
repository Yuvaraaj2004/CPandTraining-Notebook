primes = [False]*(10**6+1)
i = 2
while i*i <= len(primes):
    # print(i)
    if not primes[i]:
        for j in range(i*i, len(primes), i):
            primes[j] = True
    i += 1
primes = [i for i in range(2, len(primes)) if not primes[i]]
# print(primes)
for i in [10020, 12323, 1234, 122308, 123]:
    v = n = i
    isprime = False
    if v in primes:
        isprime = True
    fact, j = [], 0

    while primes[j]*primes[j] <= v:
        if v % primes[j] == 0:
            while v % primes[j] == 0:
                v //= primes[j]
            fact.append(primes[j])
        j += 1
    if v != 1:
        fact.append(v)
    ans, j = 0, 0

    while (isprime and primes[j] <= fact[0]) or (primes[j] < fact[0]):
        # print(n, primes[j], primes[j]*n)
        ans += n*primes[j]
        j += 1

    print(fact, v, ans)
