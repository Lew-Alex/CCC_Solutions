l = sorted([list(map(int, input().split())) for i in range(int(input()))], key=lambda x: x[0])
print(max([abs(l[i][1] - l[i-1][1]) / abs(l[i][0] - l[i-1][0]) for i in range(1, len(l))]))