import random


def randomizeMap(somMap):
    for i in range(20):
        for h in range(20):
            array = [None] * 80
            for j in range(80):
                array[j] = random.random()
            somMap[i][h] = array





print "Hello, world!"
a = 20
b = 20

somMap = [[0 for x in range(b)]for y in range(a)]
randomizeMap(somMap)
dataArr = []
learningRate = 0.9
