inputSeats = open('input5.txt', 'r').read().splitlines()

ids = [
    int(x.translate("".maketrans("FBLR", "0101")), 2)
    for x in [x.strip() for x in inputSeats]
]

print(max(ids))

myId = 0
count = 0

for x in range(len(ids)):
    if x in ids:
        print('IN')
    else:
        print('NOT IN')
        myId = x
print(myId)
