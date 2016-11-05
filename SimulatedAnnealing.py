from Solution import *
from copy import *
from math import exp
from random import random
from threading import Thread

class SimulatedAnnealing(Thread):
	"docstring for SimulatedAnnealing"
	def __init__(self, solution, resultQueue, iterations = 100, perturbations = 40, T0 = 90, alpha = 0.98):
		Thread.__init__(self)
		self.resultQueue = resultQueue
		self.solution = solution
		self.iterations = iterations
		self.perturbations = perturbations
		self.alpha = alpha
		self.T = T0

	def run(self):
		bestSolution = deepcopy(self.solution)
		currentSolution = deepcopy(self.solution)


		for it in range(self.iterations):
			for per in range(self.perturbations):
				newSolution = deepcopy(currentSolution)
				newSolution.disturb();
				delta = newSolution.getCost() - currentSolution.getCost()
				if delta <= 0:
					currentSolution = deepcopy(newSolution)
				else:
					prob = exp(-delta/self.T)
					randValue = random()
					if randValue < prob:
						currentSolution = deepcopy(newSolution)
				
				if currentSolution.getCost() < bestSolution.getCost():
					bestSolution = deepcopy(currentSolution)

			self.T = self.alpha * self.T
		print "Trhead:", self.ident, "END"
		self.resultQueue.put(bestSolution)
