from random import *

class Vehicle:
	"Vehicle with its route and capacity"
	def __init__(self, capacity):
		self.route = []
		self.capacity = capacity
		self.leftCapacity = capacity
		self.distance = 0
		self.lastDistance = 0

	def __str__(self):
		string = ""
		for c in self.route:
			string += c.__str__() + " "
		return string

	def appendCity(self, city):
		if(city.demand <= self.leftCapacity):
			self.leftCapacity -= city.demand
			if len(self.route) > 0:
				self.distance -= self.lastDistance
				self.distance += self.route[len(self.route) - 1] - (city)
				self.lastDistance = city - (self.route[0])
				self.distance += self.lastDistance
			self.route.append(city)
			return True
		else:
			return False

	def insertCity(self, i, city):
		if i == len(self.route):
			return self.appendCity(city)
		elif city.demand <= self.leftCapacity:
			self.leftCapacity -= city.demand
			lenght = len(self.route)
			previousCity = self.route[i-1]
			nextCity = self.route[i]
			self.distance -= nextCity - (previousCity)
			self.distance += city - (previousCity)
			self.distance += city - (nextCity)
			self.route.insert(i, city)
			return True
		else:
			return False
	
	def popCity(self, i):
		city = self.route.pop(i)
		self.leftCapacity += city.demand
		lenght = len(self.route)
		previousCity = self.route[i-1]
		nextCity = self.route[i%lenght]
		self.distance -= city - (previousCity)
		self.distance -= city - (nextCity)
		if i == lenght:
			self.lastDistance = previousCity - (self.route[0])
		self.distance += previousCity - (nextCity)
		return city

	def isEmpty(self):
		return len(self.route) <= 1

	def adjustDistance(self):
		self.distance = 0
		for c in range(len(self.route)):
			c1 = self.route[c]
			c2 = self.route[(c+1)%len(self.route)]
			self.distance += c1 - c2

	def reverse(self):
		if len(self.route) < 3:
			return False

		aux = range(1, len(self.route))
		index1 = choice(aux)
		aux.remove(index1)
		index2 = choice(aux)
		
		if index2 < index1:
			aux = index1
			index1 = index2
			index2 = aux

		index2 += 1
		aux = self.route[index1:index2]
		aux.reverse()
		self.route[index1:index2] = aux

		self.adjustDistance()

		return True

	def reposition(self):
		if len(self.route) < 3:
			return False

		aux = range(1, len(self.route))
		indexFrom = choice(aux)
		aux.remove(indexFrom)
		city = self.popCity(indexFrom)
		indexTo = choice(aux)
		
		while indexFrom == indexTo:
			indexTo = randint(1, len(self.route) - 1)

		self.insertCity(indexTo, city)
		return True

def popRandom(l):
	ind = randint(0, len(l)-1)
	return l.pop(ind)

def initVehicle(capacity, left, dep):
	if len(left) == 0:
		return False
	v = Vehicle(capacity)
	v.appendCity(dep)
	while len(left)>0:
		city = popRandom(left)
		if not v.appendCity(city):
			left.append(city)
			break
	return v