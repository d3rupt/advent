yas = open('input6.txt').read().splitlines()
yasgroups = []
ygroup = []
ttotal = 0
yasgroups = [line.split('\n') for line in [yasgroup.strip() for yasgroup in open('input6.txt').read().split('\n\n')]]

for yasgroup in yasgroups:
    total = sum([len(set(''.join(yasgr for yasgr in yasgroup)))])
    ttotal += total
print(ttotal)
