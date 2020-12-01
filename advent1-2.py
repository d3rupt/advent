inputNums = open('inputNums.txt', 'r').readlines()
adventList = []
results = []
print(inputNums)

for n in inputNums:
    n = int(n.replace('\n', ''))
    adventList.append(n)
print(adventList)

for a in adventList:
    for b in adventList:
        if a + b == 2020:
            print('Found one!')
            results.append([a, b])
            print(a * b)
print(results)
