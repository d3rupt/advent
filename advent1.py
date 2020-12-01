import random

inputNums = open('inputNums.txt', 'r').readlines()
adventList = []
results = []
print(inputNums)

for n in inputNums:
    n = int(n.replace('\n', ''))
    adventList.append(n)
print(adventList)

result = 0;
results = []
while result != 2020:
    pp = random.sample(adventList, 4)
    if (pp[1] + pp[2] + pp[3] == 2020):
        result = 2020
        results.append(pp[1])
        results.append(pp[2])
        results.append(pp[3])
print(results)
