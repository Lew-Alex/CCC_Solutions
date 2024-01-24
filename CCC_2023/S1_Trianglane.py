c = int(input())
l1 = list(map(int, input().split()))
prev1 = 0
l2 = list(map(int, input().split()))
prev2 = 0
sides = 0

for i in range(c):
    if l1[i] == 1 and l2[i] == 1:
        sides += 4 + 2 * (i % 2)
    elif l1[i] == 1 or l2[i] == 1:
        sides += 3
    if prev1 == 1 and l1[i] == 1:
        sides -= 2
    if prev2 == 1 and l2[i] == 1:
        sides -= 2
    prev1 = l1[i]
    prev2 = l2[i]
    # print(sides, i)

print(sides)