n = int(input())
heights = list(map(int, input().split(' ')))
width = list(map(int, input().split(' ')))
total = 0

for i in range(len(width)):
    total += min(heights[i], heights[i+1]) * width[i] + width[i] * abs(heights[i] - heights[i+1]) / 2
print(total)