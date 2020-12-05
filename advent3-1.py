Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore

@d3rupt
d3rupt
/
advent
1
00
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
advent/advent3-1.py /
@d3rupt
d3rupt Finally got it with much handholding
Latest commit 5db2c87 1 hour ago
 History
 1 contributor
8 lines (4 sloc)  262 Bytes


inputNums = open('input3.txt', 'r').read().splitlines()


def num_trees(xdist):
    return len(list(filter(lambda x: x == "#", [inputNums[y][(xdist * y) % len(inputNums[0])] for y in range(len(inputNums))])))

print('P1: {} trees'.format(num_trees(3)))
