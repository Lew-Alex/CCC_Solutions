x = int(input())
x1 = [input().split() for i in range(x)]
y = int(input())
y1 = [input().split() for i in range(y)]
g = int(input())
c = 0
d = {} # Dictionary to store the groups

for i in range(g): # Collects all the groups
    group = input().split() # Gets the three members of a group(ex: ['Bob', 'Joe', 'Jack'])
    for m in group:
        d[m] = i # Gives each person the index of the group they are in

for i in x1: # Checks if the people are in a different group that should be in the same group
    if d[i[0]] != d[i[1]]: # Check if two people are in a different group
        c += 1 # Constraint violated


for i in y1: # Checks if the people are in the same group that should be in a different group
    if d[i[0]] == d[i[1]]: # Checks if two people are in the same group
        c += 1 # Constraint violated


print(c)