s = input()
index = 0
prev_index = 0
o = []

while index < len(s)-1:
    if not s[index].isalpha():
        if s[index] == '+': o.append([1, s[prev_index:index]])
        else: o.append([0, s[prev_index:index]])

        index += 1

        temp = ''
        while index < len(s) and s[index].isnumeric():
            temp += s[index]
            index += 1
        o[-1] = [o[-1][0], int(temp), o[-1][1]]
        prev_index = index
        index -= 1

    index += 1
for i in o:
    print(i[2], "tighten" if i[0] == 1 else "loosen", abs(i[1]))