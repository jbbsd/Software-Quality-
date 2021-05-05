import random


def generateName():
    carac = "ABCDEFGHIJ"
    NB = "123456789"
    name = "files/"
    for i in range(1, 20):
        n = random.randint(0, len(carac) - 1)
        na = random.randint(0, len(NB) - 1)
        name += carac[n]
        name += NB[na]
    name += '.txt'
    return name


def createFile(fname):
    f = open(fname, "w")
    for i in range(1, 100000):
        n = random.randint(-100000, 100000)
        if i % 20 == 0:
            f.write("\n")
        f.write(str(n) + "  ")
    f.close()


if __name__ == '__main__':
    filename = generateName()
    createFile(filename)
