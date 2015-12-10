class infiniteGrid():
	def __init__(self):
		self.position = (0,0)
		self.robotPosition = (0,0)
		self.receivedGift = {self.position : 1}

	def updatePositionAndGive(self, newPosition, robot):
		if (newPosition in self.receivedGift.keys()):
			self.receivedGift[newPosition] += 1
		else:
			self.receivedGift[newPosition] = 1

		if (robot):
			self.robotPosition = newPosition
		else:
			self.position = newPosition
# ---
def resolve(lines, part, verbose=False):
	
	ig = infiniteGrid()
	iteration = 0
	for c in lines[0]:
		if (part == '1' or iteration == 0):
			intPos = ig.position
			robot = False
		elif(part == '2' and iteration == 1):
			intPos = ig.robotPosition
			robot = True
		else:
			throw(100)

		if (c == '^'):
			ig.updatePositionAndGive((intPos[0], intPos[1]+1), robot)
		elif (c == 'v'):
			ig.updatePositionAndGive((intPos[0], intPos[1]-1), robot)
		elif (c == '<'):
			ig.updatePositionAndGive((intPos[0]-1, intPos[1]), robot)
		elif (c == '>'):
			ig.updatePositionAndGive((intPos[0]+1, intPos[1]), robot)
		else:
			throw(10)
		iteration = (iteration+1)%2

	return len(ig.receivedGift)