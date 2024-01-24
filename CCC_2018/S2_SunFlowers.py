n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

def rotate(l):
    return list(zip(*l[::-1]))

def check(l):
    for i in l:
        prev = -1
        for j in i:
            if j < prev:
                return False
            prev = i[0]
    for i in rotate(rotate(rotate(l))):
        prev = -1
        for j in i:
            if j < prev:
                return False
            prev = i[0]
    return True

while check(l) != True:
    l = rotate(l)
print('\n'.join([' '.join([str(i) for i in j]) for j in l]))
            
