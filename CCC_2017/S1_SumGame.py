n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_sum = 0
b_sum = 0
k = 0


for i in range(n):
    a_sum += a[i]
    b_sum += b[i]
    if a_sum == b_sum:
        k = i+1
print(k)