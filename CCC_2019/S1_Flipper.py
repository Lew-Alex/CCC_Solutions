s = str(input())
l = [[1, 2], [3, 4]]

def flip_h(l):
    l.reverse()
    return l
def flip_v(l):
    return [i[::-1] for i in l]

for i in s:
    if i == 'H':
        l = flip_h(l)
    elif i == 'V':
        l = flip_v(l)
for i in l:
    print(' '.join([str(j) for j in i]))
