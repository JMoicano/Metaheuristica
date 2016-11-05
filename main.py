from Util import *
from Solution import *
from SimulatedAnnealing import *
from Genetic import *
from os import walk
from numpy import std, mean
import sys
import Queue as queue
import time

def writeOutFile(file, name, times, results):
	meanTime = str(mean(times))
	standardDeviation = str(std(results))
	meanResult = str(mean(results))
	bestResult = str(min(results))
	worstResult = str(max(results))
	file.write(name + "; ; ")
	file.write(meanResult)
	file.write("; ")
	file.write(bestResult)
	file.write("; ")
	file.write(worstResult)
	file.write("; ")
	file.write(standardDeviation)
	file.write("; ; ")
	file.write(meanTime)
	file.write("\n")
	file.flush

def main(args):
	if len(args) == 4:
		k = int(args[1])
		iterations = int(args[2])
		runs = int(args[3])
		numFile = int (args[4])
		
		f = []
		for (dirpath, dirnames, filenames) in walk("Data"):
			f.extend(filenames)
			break

		files = [dirpath + "/" + filename for filename in f]
		file = files[numFile]
		cities, capacity, dep, name = readProblemFile(file)
		outName = "out" + name + ".csv"
		with open(outName, "w+") as out:
			print name
			
			times = []
			results = []
			for run in xrange(runs):
				
				print "Run:", run
				firstGeneration = []
				secondGeneration = queue.Queue()
				inicio = time.time()
				for i in xrange(k):
					solution = initSolution(capacity, cities, dep)
					firstGeneration.append(solution)
				
				best = deepcopy(firstGeneration[0])
				for it in xrange(iterations):
					print "   It:", it
					print "      Genetic"
					for i in xrange(k):
						mother = firstGeneration[i]
						aux = firstGeneration[:]
						aux.remove(mother)
						father = choice(aux)
						ga = Genetic(mother, father)
						ga.cross()

					print "      SA"
					for solution in firstGeneration:
						SA = SimulatedAnnealing(solution, secondGeneration)
						SA.start()

					for i in xrange(k):
						solution = secondGeneration.get()
						if best == None or solution.getCost() < best.getCost():
							best = deepcopy(solution)
						firstGeneration[i] = (solution)

				print "   Best:", best.getCost()
				fim = time.time()
				duracao = fim - inicio
				times.append(duracao)
				results.append(best.getCost())

			writeOutFile(out, name, times, results)

if __name__ == '__main__':
	main(sys.argv)
