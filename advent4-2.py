import re

passportsStart = open('input4.txt').read().split('\n\n')

fields = ['byr', 'iyr', 'eyr', 'ecl', 'hcl', 'hgt', 'pid']
ecl = ['amb', 'blu', 'gry', 'grn', 'brn', 'hzl', 'oth']
byr1 = 1920
byr2 = 2020

iyr1 = 2010
iyr2 = 2020

eyr1 = 2020
eyr2 = 2030

hgt = ['cm', 'in']
htcm1 = 150
hgtcm2 = 193
htin1 = 59
htin2 = 76
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

passportsDict = {}
passportCount = 0
for passports in passports2:
    passportDict = {}
    for passs in passports:
        passportDict[passs[0]] = passs[1]
    passportsDict[passportCount] = passportDict
    passportCount += 1

dictCount = 0
dictsToCheck = []

for dicts in passportsDict:
"""dictsToCheck = {}

for dicts in range(len(passportsDict) - 1):
    if len(passportsDict[dicts]) == 8:
        dictsToCheck[dicts] = passportsDict[dicts]
    if len(passportsDict[dicts]) == 7 and 'cid' not in passportsDict[dicts]:
        dictsToCheck[dicts] = passportsDict[dicts]"""

finalCount = 0
print(len(dictsToCheck))
dictsIndex = 0
for dicts in dictsToCheck:
    print(dicts)

for dicts in range(len(dictsToCheck) - 1):
    if int(dictsToCheck[dicts]['byr']) >= byr1 and int(dictsToCheck[dicts]['byr']) <= byr2:
        if int(dictsToCheck[dicts]['iyr']) >= iyr1 and int(dictsToCheck[dicts]['iyr']) <= iyr2:
            if int(dictsToCheck[dicts]['eyr']) >= eyr1 and int(dictsToCheck[dicts]['eyr']) <= eyr2:
                if dictsToCheck[dicts]['ecl'] in ecl:
                    if re.match('^#[a-f][0-9]', dictsToCheck[dicts]['hcl']):
                        if re.match('[0-9]{9}', dictsToCheck[dicts]['pid']):
                            if (re.match('cm$', dictsToCheck[dicts]['hgt']) and (int(dictsToCheck[dicts]['hgt'][:-2]) >= hgtcm1 or int(dictsToCheck[dicts]['hgt'][:-2]) <= hgtcm2)) or (re.match('in$', dictsToCheck[dicts]['hgt']) and (int(dictsToCheck[dicts]['hgt'][:-2]) >= hgtin1 or int(dictsToCheck[dicts]['hgt'][:-2]) <= hgtin2)):
                                if re.match('[0-9]{9}', dictsToCheck[dicts]['pid']):
                                    finalCount += 1
print('FINAL COUNT: ' + str(finalCount))
