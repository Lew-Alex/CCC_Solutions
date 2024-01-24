s1, s2 = [input(), input()]

for i in s2:
    if i in s1:
        s1 = s1.replace(i, '', 1)
        s2 = s2.replace(i, '', 1)

if sum([1 if i != '*' else 0 for i in s2]) == 0: print('A')
else: print('N')