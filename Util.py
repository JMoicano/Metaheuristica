from string import *
from City import *

def readParse(file, sep):
	line = file.readline().strip()
	parse = line.partition(sep)
	return parse[2]

def readProblemFile(fileName):
	with open(fileName, "r+") as file:
		name = readParse(file, " : ")
		
		file.readline()
		file.readline()
		
		dimension = int(readParse(file, " : "))
		file.readline()
		
		capacity = int(readParse(file, " : "))
		file.readline()
		
		coords = []
		for i in range(dimension):
			cityParse = readParse(file, " ")
			coordParse = cityParse.partition(" ")
			x = float(coordParse[0])
			y = float(coordParse[2])
			coords.append([x, y])
		file.readline()
		
		cities = []		
		for i in range(dimension):
			demand = int(readParse(file, " "))
			city = City(coords[i][0], coords[i][1], demand)
			cities.append(city)
			if demand == 0:
				dep = i

		return cities, capacity, dep, name