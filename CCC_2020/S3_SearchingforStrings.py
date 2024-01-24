h, n, d = sorted(input()), input(), []

for i in range(len(n)-len(h)+1):
    cur = n[i:i+len(h)]
    if sorted(cur) == h and cur not in d: d.append(cur)

print(len(d))
