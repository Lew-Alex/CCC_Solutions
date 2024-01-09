t = int(input())
n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l1.sort()
l2.sort()
o = 0

if t == 1:
    for i in range(n):
        o += max(l1[i], l2[i])
else:
    l2.reverse()
    for i in range(n):
        o += max(l1[i], l2[i])
print(o)