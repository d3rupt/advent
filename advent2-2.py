inputNums = open('input2.txt', 'r').readlines()
adventList = []
firstPass = []

countRange = []
letter = []
strings = []

results = []

for n in inputNums:
    n = n.replace('\n', '')
    adventList.append(n)
    n = n.split(' ')
    firstPass.append(n)

for f in firstPass:
    f0 = f[0].split('-')
    f0[0] = int(f0[0])
    f0[1] = int(f0[1])
    countRange.append(f0)

    f1 = f[1].replace(':', '')
    letter.append(f1)

    f2 = f[2]
    strings.append(f2)

for a, b, c in zip(countRange, letter, strings):
    index1 = a[0] - 1
    index2 = a[1] - 1
    print(c[index1], c[index2], b, c)
    if c[index1] == b:
        if c[index2] != b:
            results.append(c)
    elif c[index1] != b:
        if c[index2] == b:
            results.append(c)

print('{} passwords match.' .format(len(results)))
