s = str(input())
r = int(input())
c = int(input())
g = []
words = 0
for i in range(r):
    g.append(list(map(str, input().split())))

checks = [[1, 1], [0, 1], [-1, -1], [1, -1], [-1, 1], [1, 0], [-1, 0], [0, -1]]
def get_opposite(k): # Gets the perpendicular direction
    if 0 in k:
        if k[0] == 0:
            k[1] = 0
            return [[1, k[1]], [-1, k[1]]]
        else:
            k[0] = 0
            return [[k[0], 1], [k[0], -1]]
    else:
        return [[k[0], -k[1]], [-k[0], k[1]]]
    

def check_around(x, y, letter):
    o = []
    for i in checks:
         if i[0] + x >= 0 and i[0] + x < r and i[1] + y >= 0 and i[1] + y < c:
             if g[i[0]+x][i[1]+y] == letter:
                o.append(i)
    return o

def find_word(x, y, angle, dir, index):
    global words
    around = check_around(x, y, s[index]) 
    if dir in around:
        if index == len(s)-1: 
            words += 1
        else: 
            find_word(dir[0]+x, dir[1]+y, angle, dir.copy(), index+1)
    if angle == False and index != 1:
        opp = get_opposite(dir)
        if (index == len(s)-1):
            if opp[0] in around:
                words += 1
            if opp[1] in around:
                words += 1
        else:  
            if opp[1] in around: 
                find_word(opp[1][0]+x, opp[1][1]+y, True, opp[1].copy(), index+1)
            if opp[0] in around: 
                find_word(opp[0][0]+x, opp[0][1]+y, True, opp[0].copy(), index+1)
    



for i in range(r):
    for j in range(c):
        if s[0] == g[i][j]:
            for k in check_around(i, j, s[1]):
                # print(i, j, k)
                find_word(i, j, False, k.copy(), 1)
                
if s[0] == s[len(s)-1]: # To ensure it doesn't double count
    words = words//2
print(words)


'''



HII
3
3
I I I 
H H H
I I I
'''