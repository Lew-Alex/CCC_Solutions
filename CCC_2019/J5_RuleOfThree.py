conv1 = tuple(map(str, input().split(' ')))
conv2 = tuple(map(str, input().split(' ')))
conv3 = tuple(map(str, input().split(' ')))
a_conv = [conv1, conv2, conv3]
l = list(map(str, input().split(' ')))
l[0] = int(l[0])

def conv(num, index, string):
    # Assuming this conversion is possible
    string = string[:index] + a_conv[num][1] + string[index+len(a_conv[num][0]):]
    
    return string

def find_conv(string):
    indexes = []
    for i in range(len(string)):
        for index, conv in enumerate(a_conv):
            if len(string) - i >= len(conv[0]):
                if string[i:i+len(conv[0])] == conv[0]:
                    indexes.append([i, index])
    return indexes

strings = [l[1]]
steps = [[]]
counter = 0
while l[2] not in strings:
    new_strings = []
    new_steps = []
    counter += 1
    # print(counter)
    for i, step in zip(strings, steps):
        c = find_conv(i)

        for j in c:
            j.append(conv(j[1], j[0], i))
            new_strings.append(j[2])

            new_step = step.copy()
            new_step.append([j[1]+1, j[0]+1, j[2]])
            new_steps.append(new_step)
    strings = new_strings
    steps = new_steps
    print(len(strings))
    if l[2] in strings or counter > l[0]+2:
        print(strings)
        # print(steps[strings.index(l[2])])
        for i in steps[strings.index(l[2])]:
            print(i[0], i[1], i[2])
        break



'''
AAB ABBA
B AA
BA BBB
10 AABBBAABAB AAAAAABBBABBABBBABAB

AA AB
AB BB
B AA
4 AB AAAB
'''