class Point(object):
	"Euclidian point"
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(%.3f, %.3f)" %(self.x, self.y)
	
	def __sub__(self, p):
		return int(((self.x - p.x)**2 + (self.y - p.y)**2)**(.5)+0.5)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

class City(Point):
	"City with its location and demand"
	def __init__(self, x, y, demand):
		self.demand = demand
		super(City, self).__init__(x,y)

