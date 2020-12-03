inputNums = open('input3.txt', 'r').readlines()
slopesList = []
firstPass = []
countRange = []
trees = 0
slope1 = 3
slope2 = 1
curIndex = 0
count = 0
for i in inputNums:
    i = i.replace('\n', '')
    slope = i[curIndex:curIndex + 3]
    print(slope)
    for s in slope:
        if s == '#':
            trees += 1
            print('trees +1')
    curIndex += 3
    print('Trees:' + str(trees))
    #print('slope: {}; curIndex: {}' .format(slope, curIndex))
    count += 1
print('{} trees' .format(trees))
