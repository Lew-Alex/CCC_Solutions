s = str(input())
l, m, r = 0, 0, 0
t = []
for i in s:
    if i == 'L': l += 1
    elif i == 'M': m += 1
    else: r += 1
    t.append(i)
s = t

o = 0
for i in range(l):
    if s[i] != 'L':
        o += 1
        s[len(s) - s[::-1].index('L') - 1] = s[i]
        s[i] = 'L'
for i in range(l, l+m):
    if s[i] != 'M':
        o += 1
        s[len(s) - s[::-1].index('M') - 1] = s[i]
        s[i] = 'M'
print(o)