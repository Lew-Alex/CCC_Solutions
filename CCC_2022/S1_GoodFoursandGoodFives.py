n = int(input())
counter = 0

for i in range(0, n+1, 4):
    if (n-i)%5 == 0:
        counter += 1
print(counter)
