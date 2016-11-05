from copy import *
from random import *

class Genetic(object):
	"Genetic algorithm"
	def __init__(self, mother, father):
		self.mother = mother
		self.father = father

	def cross(self):
		index = randint(0, len(self.father.fleet) - 1)
		gene = deepcopy(self.father.fleet[index])
		self.mother.appendVehicle(gene)
		