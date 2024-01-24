n = int(input())
p = []
w = []
d = []
for i in range(n):
    cur = list(map(int, input().split(' ')))
    p.append(cur[0])
    w.append(cur[1])
    d.append(cur[2])

def calc(c):
    t = sum(max(0, abs(c - p_val) - d_val) * w_val for p_val, d_val, w_val in zip(p, d, w))
    return t

cur = (min(p)+max(p))//2
counter = 0
while (calc(cur) > calc(cur+1) or calc(cur) > calc(cur-1)):
    counter += 1
    if calc(cur+1) < calc(cur-1):
        cur += max(n//2**counter, 1)
    else:
        cur -= max(n//2**counter, 1)
print(calc(cur))