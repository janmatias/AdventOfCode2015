import sys, itertools

class Graph():
	def __init__(self):
		self.locs = set()
		self.costDict = {}

	def add(self, node1, node2, cost):
		self.locs.add(node1)
		self.locs.add(node2)
		if (node1 in self.costDict):
			self.costDict[node1][node2] = cost
		else:
			self.costDict[node1] = {node2 : cost}

		if (node2 in self.costDict):
			self.costDict[node2][node1] = cost
		else:
			self.costDict[node2] = {node1 : cost}

	def traverse(self, order):
		traversalCost = 0
		for i in range(len(order)-1):
			currentTraversal = (order[i], order[i+1])
			traversalCost += self.costDict[currentTraversal[0]][currentTraversal[1]]
		return traversalCost


# ---
def resolve(lines, part):
	graph = Graph()
	for line in lines:
		p1, _, p2, _, cost = line.split(" ")
		graph.add(p1, p2, int(cost))
	
	traversalCost = sys.maxsize
	decider = min
	if (part == '2'):
		traversalCost = -sys.maxsize
		decider = max
	for permutation in (itertools.permutations(graph.locs)):
		traversalCost = decider(graph.traverse(permutation), traversalCost)
	return traversalCost
