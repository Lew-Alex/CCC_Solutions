n = int(input())
t = int(input())
trees = [list(map(int, input().split())) for i in range(t)]
o = 0
f_g = []

def populate(x, y, w):
    g = [[x, y]]
    if max(x+w, y+w) > (n+1):
        return False
    for i in range(1, w):
        for a in range(i+1):
            g.append([x+i, y+a])
            g.append([x+a, y+i])
    for i in trees:
        if i in g:
            return False
    return g

x = 0
y = 0
for x in range(1, n+1):
    for y in range(1, n+1):
        for w in range(o, n+1):
            g = populate(x, y, w)
            if g:
                o = w
            else:
                break
                
        
print(o)

