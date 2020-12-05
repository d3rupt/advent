passportsStart = open('input4.txt').read().split('\n\n')

passports = []
passports1 = []
passports4 = []
passports2 = []

for p in passportsStart:
    p = p.replace('\n', ' ')
    passp = p.split(' ')
    passports.append(passp)

for p in passports:
    passports3 = []
    for q in p:
        r = q.split(':')
        passports3.append(r)
    passports2.append(passports3)
coolPassports = 0

passportsDict = {}
passportCount = 0
for passports in passports2:
    passportDict = {}
    for passs in passports:
        passportDict[passs[0]] = passs[1]
    passportsDict[passportCount] = passportDict
    passportCount += 1
    dictCount = 0
for dicts in range(len(passportsDict)):
        if len(passportsDict[dicts]) == 8:
            coolPassports += 1
        if len(passportsDict[dicts]) == 7 and 'cid' not in passportsDict[dicts]:
            coolPassports += 1
        dictCount += 1
print(coolPassports)
print(len(passportsDict))
