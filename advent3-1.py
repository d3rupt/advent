
inputNums = open('input3.txt', 'r').read().splitlines()


def num_trees(xdist):
    return len(list(filter(lambda x: x == "#", [inputNums[y][(xdist * y) % len(inputNums[0])] for y in range(len(inputNums))])))

print('P1: {} trees'.format(num_trees(3)))
