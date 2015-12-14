class Reindeer():
	def __init__(self, name, speed, runningTime, restingTime):
		self.name = name
		self.speed = speed
		self.runningTime = runningTime
		self.restingTime = restingTime
		self.currentRunTime = 0
		self.currentRestTime = 0
		self.distance = 0
		self.points = 0

	def run(self):
		if (self.currentRunTime < self.runningTime):
			self.currentRunTime += 1
			self.distance += self.speed
		# Here self.currentRunTime == self.runningTime
		elif (self.currentRestTime < self.restingTime):
			self.currentRestTime += 1
		# Here self.currentRestTime == self.restingTime
		else:
			self.currentRunTime = 1
			self.distance += self.speed
			self.currentRestTime = 0

def race(reindeer, time):
	for i in range(time):
		maxDistance = -1
		for r in reindeer:
			r.run()
			if (r.distance > maxDistance):
				maxDistance = r.distance
		for r in reindeer:
			if (r.distance == maxDistance):
				r.points += 1
	return findWinningDistanceAndScore(reindeer)

def findWinningDistanceAndScore(reindeer):
	maxDistance = -1
	maxPoints = -1
	for r in reindeer:
		if (r.distance > maxDistance):
			maxDistance = r.distance
		if (r.points > maxPoints):
			maxPoints = r.points

	return (maxDistance, maxPoints)

# ---
def resolve(lines, part):
	print("test")
	reindeer = []
	# parse text input
	for line in lines:
		line = line.split(" ")
		reindeer.append(Reindeer(line[0], int(line[3]), int(line[6]), int(line[13])))
	
	# Simulate the race
	winnerTuple = race(reindeer, 2503)
	return winnerTuple[int(part)-1]