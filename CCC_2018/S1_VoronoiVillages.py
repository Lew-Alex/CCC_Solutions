n = int(input())
v = []
for i in range(n):
    v.append(int(input())) 
v.sort()
o = v[len(v)-1]-v[0]

for i in range(1, len(v)-1):
    o = min(o, (v[i+1]-v[i]+v[i]-v[i-1])/2)
print(o)