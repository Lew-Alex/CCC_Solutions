n = int(input())
d = {}
for i in list(map(int, input().split())):
    if not i in d: d[i] = 1
    else: d[i] += 1

o = 0
m = 0
t = -1
for i in range(max(d)*2+1):
    
    for e in d:
        if i-e in d:
            o += min(d[e], d[i-e])
    o /= 2
    if o > m:
        m = o
        t = 1
    elif o == m: 
        t += 1
    o = 0
        
print(int(m), t)
