n = int(input())
l = list(map(int, input().split()))
l.sort()
o = []
if n % 2 == 1:
    outlier = l.pop(0)

for i in range(len(l)//2):
    print(l[len(l)//2-i-1], end=' ')
    print(l[len(l)//2+i], end =' ')

if n % 2 == 1:
    print(outlier, end="")
print()