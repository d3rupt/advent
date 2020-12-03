inputNums = open('input3.txt', 'r').readlines()
slopesList = []
firstPass = []
countRange = []
trees = 0
slope1 = 3
slope2 = 1
curIndex = 0
for i in inputNums:
    nextIndex = inputNums.index(i) + 1
    i = i.replace('\n', '')
    print('curIndex: ' + str(curIndex))
    slope = i[curIndex:curIndex + 3]
    print('SLOPE LENGTH: ' + str(len(slope)))
    if len(slope) < 3:
        print('End of line!')
        print('slope length: ' + str(len(slope)))
        slopeDiff = (3 - len(slope))
        nextLine = inputNums[nextIndex][:slopeDiff]
        print(nextLine)
        slope = slope + str(nextLine)
        print('new slope length: ' + str(len(slope)))
        curIndex = 0 + (slopeDiff)
        print('curIndex: ' + str(curIndex))
    for s in slope:
        if s == '#':
            trees += 1
    curIndex += 3
print('{} trees' .format(trees))
