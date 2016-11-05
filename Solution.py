from random import *
from copy import *
from Vehicle import *

class Solution:
	"Solution to the CVRP"
	def __init__(self, dep):
		self.fleet = []
		self.dep = dep

	def __str__(self):
		string = ""
		for v in self.fleet:
			string += v.__str__() + "\n"
		return string

	def appendVehicle(self, vehicle):
		cityList = vehicle.route[:]
		for v in self.fleet:
			for c in v.route:
				if c == v.route[0]:
					continue
				if cityList.count(c) > 0:
					ci = v.route.index(c)
					v.popCity(ci)
					if v.isEmpty():
						self.fleet.remove(v)
		self.fleet.append(vehicle)
		
	def popVehicle(self, i):
		return self.fleet.pop(i)

	def getCost(self):
		cost = 0
		for v in self.fleet:
			cost += v.distance
		return cost

		

	def switch(self):
		
		vehicle1 = choice(self.fleet)
		aux = self.fleet[:]
		aux.remove(vehicle1)
		vehicle2 = choice(aux)

		aux = vehicle1.route[1:]
		city1 = choice(aux)

		aux = vehicle2.route[1:]
		city2 = choice(aux)

		city1Index = vehicle1.route.index(city1)

		city2Index = vehicle2.route.index(city2)

		vehicle1.popCity(city1Index)
		if not vehicle1.insertCity(city1Index, city2):
			vehicle1.insertCity(city1Index, city1)
			return False

		vehicle2.popCity(city2Index)
		if not vehicle2.insertCity(city2Index, city1):
			vehicle1.popCity(city1Index)
			vehicle1.insertCity(city1Index, city1)
			vehicle2.insertCity(city2Index, city2)
			return False

		return True

	def tradeRoutes(self):
		vehicle1Index = randint(0, len(self.fleet) - 1)
		vehicle2Index = randint(0, len(self.fleet) - 1)

		while vehicle1Index == vehicle2Index:
			vehicle2Index = randint(0, len(self.fleet) - 1)
		
		vehicle1 = self.fleet[vehicle1Index]
		vehicle2 = self.fleet[vehicle2Index]

		if len(vehicle1.route) < 3 or len(vehicle2.route) < 3:
			return False

		route1Index1 = randint(1, len(vehicle1.route) - 1)
		route1Index2 = randint(1, len(vehicle1.route) - 1)

		while route1Index1 == route1Index2:
			route1Index2 = randint(1, len(vehicle1.route) - 1)

		if route1Index1 > route1Index2:
			aux = route1Index1
			route1Index1 = route1Index2
			route1Index2 = aux

		route1 = []
		for r1 in range(route1Index2 - route1Index1):
			route1.append(vehicle1.popCity(route1Index1))

		if len(vehicle1.route) == 1:
			self.popVehicle(vehicle1Index)

		route2Index1 = randint(1, len(vehicle2.route) - 1)
		route2Index2 = randint(1, len(vehicle2.route) - 1)

		while route2Index1 == route2Index2:
			route2Index2 = randint(1, len(vehicle2.route) - 1)

		if route2Index1 > route2Index2:
			aux = route2Index1
			route2Index1 = route2Index2
			route2Index2 = aux

		route2 = []
		for r2 in range(route2Index2 - route2Index1):
			route2.append(vehicle2.popCity(route2Index1))

		if len(vehicle2.route) == 1:
			self.popVehicle(vehicle2Index)

		self.addSubRoute(route1, vehicle1)
		
		self.addSubRoute(route2, vehicle1)
		return True

	def disturb(self):
		case = randint(0, 3)
		if case == 0:
			while not self.switch():
				pass
		elif case == 1:
			vehicle = randint(0, len(self.fleet) - 1)
			while not self.fleet[vehicle].reverse():
				vehicle = randint(0, len(self.fleet) - 1)
		elif case == 2:
			vehicle = randint(0, len(self.fleet) - 1)
			while not self.fleet[vehicle].reposition():
				vehicle = randint(0, len(self.fleet) - 1)
		elif case == 3:
			while not self.tradeRoutes():
				pass

	def addSubRoute(self, route, vehicle):
		vehicleCount = 0
		for ci in range(len(route)):
				c = route[ci]
				count = 0
				while not vehicle.appendCity(c):
					if count == len(vehicle.route):
						left = deepcopy(route[ci:])
						v = initVehicle(vehicle.capacity, left, vehicle.route[0])
						self.appendVehicle(v)
						return
					else:
						vehicle = self.fleet[vehicleCount%len(self.fleet)]
						vehicleCount += 1
					#count += 1

def initSolution(capacity, cities, dep):
	left = cities[:]
	left.pop(dep)
	s = Solution(dep)
	while len(left) > 0:
		v = initVehicle(capacity, left, cities[dep])
		s.appendVehicle(v)
	return s