m = int(input())
n = int(input())
k = int(input())
r = [0]*m
c = [0]*n


for i in range(k):
    cur = input().split()
    cur[1] = int(cur[1])-1
    if cur[0] == 'R':
        r[cur[1]] = sum([1 if r[cur[1]] == 0 else 0])
    else:
        c[cur[1]] = sum([1 if c[cur[1]] == 0 else 0])

print(sum(r)*n + sum(c)*m - 2*(sum(c) * sum(r)))
