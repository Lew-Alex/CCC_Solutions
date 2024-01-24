t = int(input())
inputs = []
d = {}

sieve = [1]*2000002
sieve[0] = 0
sieve[1] = 0
primes = [2]

for i in range(2, 2000002, 2):
    sieve[i] = 0

for i in range(3, 2000002, 2):
    if sieve[i]:
        primes.append(i)
        for j in range(i * i, 2000002, i + i):
            sieve[j] = 2000002


for i in range(t): inputs.append(int(input()))

for input in inputs:
    total = input * 2
    for i in range(len(sieve)):
        if sieve[i] == 1 and sieve[total - i] == 1:
            print(i, total - i)
            break



