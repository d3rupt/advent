inputSeats = open('input5.txt', 'r').read().splitlines()

ids = [
    int(x.translate("".maketrans("FBLR", "0101")), 2)
    for x in [x.strip() for x in inputSeats]
]

print(max(ids))
