passportsStart = open('input4.txt').read().split('\n\n')

fields = ['byr', 'iyr', 'eyr', 'ecl', 'hcl', 'hgt', 'pid']
ecl = ['amb', 'blu', 'gry', 'grn', 'brn', 'hzl', 'oth']
hcl = ['a', 'b', 'c', 'd', 'e', 'f']
byr1 = 1920
byr2 = 2002

iyr1 = 2010
iyr2 = 2020

eyr1 = 2020
eyr2 = 2030

hgt = ['cm', 'in']
hgtcm1 = 150
hgtcm2 = 193
hgtin1 = 59
hgtin2 = 76
passports = []
passports1 = []
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

passportsDict = []
passportCount = 0
for passports in passports2:
    passportDict = {}
    for passs in passports:
        passportDict[passs[0]] = passs[1]
    passportsDict.append(passportDict)
    passportCount += 1
print(passportsDict)
dictCount = 0
dictsToCheck = []

"""dictsToCheck = {}

for dicts in range(len(passportsDict) - 1):
    if len(passportsDict[dicts]) == 8:
        dictsToCheck[dicts] = passportsDict[dicts]
    if len(passportsDict[dicts]) == 7 and 'cid' not in passportsDict[dicts]:
        dictsToCheck[dicts] = passportsDict[dicts]"""
finalCount = 0
dictsIndex = 0
for dicts in passportsDict:
    if len(dicts) == 8:
        dictsToCheck.append(dicts)
    elif len(dicts) == 7 and 'cid' not in dicts.keys():
        dictsToCheck.append(dicts)
    #rint(dicts)
for dicts in dictsToCheck:
    if int(dicts['byr']) >= byr1 and int(dicts['byr']) <= byr2:
        print('BYR')
        if int(dicts['iyr']) >= iyr1 and int(dicts['iyr']) <= iyr2:
            print('IYR')
            if int(dicts['eyr']) >= eyr1 and int(dicts['eyr']) <= eyr2:
                print('EYR')
                if dicts['hcl'][0] == '#':
                    for d in dicts['hcl'][1:]:
                        print(len(dicts['hcl'][1:]))
                        if (d.isnumeric() or d in hcl) and len(d) == 6:
                            print('HCL')
                    if dicts['ecl'] in ecl:
                        print('ECL')
                        if len(dicts['pid']) == 9 and int(dicts['pid']):
                            print('PID')
                            if dicts['hgt'][-2:] == 'cm':
                                if int(dicts['hgt'][:-2]) >= hgtcm1 and int(dicts['hgt'][:-2]) <= hgtcm2:
                                    print('HGT')
                                    finalCount += 1
                            elif dicts['hgt'][-2:] == 'in':
                                if int(dicts['hgt'][:-2]) >= hgtin1 and int(dicts['hgt'][:-2]) <= hgtin2:
                                    print('HGT')
                                    finalCount += 1
                            else:
                                print('ERRORHGT: ' + dicts['hgt'])
                        else:
                            print('ERRORPID: ' + dicts['pid'])
                    else:
                        print('ERRORECL: ' + dicts['ecl'])
                else:
                    print('ERRORHCL: ' + dicts['hcl'])
            else:
                print('ERROR EYR: ' + dicts['eyr'])
        else:
            print('ERROR IYR: ' + dicts['iyr'])
    else:
        print('ERROR BYR: ' + dicts['byr'])
print('FINAL COUNT: ' + str(finalCount))
