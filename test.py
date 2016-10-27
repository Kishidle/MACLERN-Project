#Coded by Arca, Garcia


import random
import numpy
import csv
class SOMNode:
    def __init__(self, weights, eucDistance):
        self.weights = weights
        self.eucDistance = eucDistance
class dataInput:
    def __init__(self, attributes):
        self.attributes = attributes


def randomizeMap(somMap):
    for i in range(20):
        for h in range(20):
            array = [None] * 80
            for j in range(80):
                array[j] = random.random()
            node = SOMNode(array, 0)
            somMap[i][h] = node





print "Hello, world!"
a = 20
b = 20

somMap = [[0 for x in range(b)]for y in range(a)]
with open('csvhere.csv', 'rU') as data: #i dont know anymore
    reader = csv.reader(data)
    next(reader) #to skip header
    for row in reader:
        yield [float(i) for i in row]
        #how to read CSV
dataArr = [] #get from csv file
learningRate = 0.9
radius = 20
randomizeMap(somMap)
iteration = 0 #placeholder
radChange = iteration / a
radIter = 0;


#get a random input from the input data, compare its euclidean distance with the weights, get the smallest distance to find the winning neighborhood
#adjust weights in winning neighborhood with formula, then change learning rate and change radius(if needed)

for x in range(iteration): #do SOM algorithm^
    n = random.randrange(0, 10000)
    for i in range(20):
        for h in range(20):
            if i == 0 and h == 0:
                dist = numpy.linalg.norm(dataArr[n], somMap[i][h].weights) #i looked in stackoverflow and they say this is the same as computing the euclidean distance
                winA = i
                winB = h
            elif numpy.linalg.norm(dataArr[n], somMap[i][h].weights) < dist:
                dist = numpy.linalg.norm(dataArr[n], somMap[i][h].weights)
                winA = i
                winB = h
    for i in range(iteration, 0, -1): #start, end, step
