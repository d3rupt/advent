inputNums = open('input2.txt', 'r').readlines()
adventList = []
firstPass = []
print(inputNums)
countRange = []
letter = []
strings = []
results = [

]
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
    print(f0)

    f1 = f[1].replace(':', '')
    letter.append(f1)
    print(f1)

    f2 = f[2]
    strings.append(f2)
    print(f2)

for a, b, c in zip(countRange, letter, strings):
    print(a[0], a[1], b, c)
    if c.count(b) >= a[0] and c.count(b) <= a[1]:
        results.append(c)

print('{} passwords match.' .format(len(results)))
