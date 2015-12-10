import sys, copy

class Node():
	def __init__(self, id):
		self.id = id
		self.children = {}
		self.distance = sys.maxsize

def djikstra(initialNode, allNodes):
	unvisited = copy.deepcopy(allNodes)
	visited = {}
	current = initialNode
	current.distance = 0
	print(current.id + "---id---")

	while (len(unvisited) > 0):
		print("Current: " + current.id)
		costToCurrent = current.distance
		for n in unvisited.values():
			if (n.id in current.children and n.id != current.id):
				costToNext = current.children[n.id]
				fullCostToNext = n.distance

				if (costToCurrent + costToNext < fullCostToNext):
					n.distance = costToCurrent + costToNext
					print("node: " + n.id + " set distance to: " + str(n.distance))
		
		visited[current.id] = unvisited[current.id]
		del unvisited[current.id]
		current = getNodeWithLowestCost(unvisited)

	return getNodeWithHighestCost(visited).distance
	

def getNodeWithLowestCost(nodes):
	minNode = None
	minValue = sys.maxsize
	for n in nodes.values():
		print(n.distance)
		if (n.distance < minValue):
			minValue = n.distance
			minNode = n
	return minNode

def getNodeWithHighestCost(nodes):
	maxNode = None
	maxValue = -1
	for n in nodes.values():
		print ("maxFor- " + n.id + " - " + str(n.distance))
		if (n.distance > maxValue):
			maxValue = n.distance
			maxNode = n
	print("returning max: " + str(maxNode.distance))
	return maxNode

# ---
def resolve(lines, part):
	nodes = {}
	for line in lines:
		ls = line.split(" ")
		fromCity = ls[0]
		toCity = ls[2]
		cost = int(ls[4])

		if (fromCity not in nodes.keys()):
			nodes[fromCity] = Node(fromCity)
			print("Generating: " + fromCity)
		nodes[fromCity].children[toCity] = cost
		print("Adding " + str(cost) + " to children of " + fromCity + ".  toCity == " + toCity)

		if (toCity not in nodes.keys()):
			nodes[toCity] = Node(toCity)
			print("Generating: " + toCity)
		nodes[toCity].children[fromCity] = cost
		print("Adding " + str(cost) + " to children of " + toCity + ".  fromCity == " + fromCity)


	minimum = sys.maxsize
	for k in nodes.keys():
		print(nodes[k].id + " - " + str(nodes[k].children))
	for id, node in nodes.items():
		print ("iterating...\n")
		#print(nodes)
		unvisited = copy.deepcopy(nodes)
		minimum = min(minimum, djikstra(copy.deepcopy(node), unvisited))
	return minimum