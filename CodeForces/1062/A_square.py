f = open('inputs.txt', 'r')
first = f.readline() # skip the number of test cases
line = f.readline()
while line:
    line = line.split() # split "1 2 3 4" into ['1','2','3','4']
    if len(set(line)) == 1: # set removes duplicates, so 4 equal values = 1 unique element
        print("YES")
    else:
        print("NO")
    line = f.readline()
f.close()

t = int(input())
for _ in range(t):
    line = input().split()
    if len(set(line)) == 1:
        print("YES")
    else:
        print("NO")
