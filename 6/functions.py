class LightGrid():
	def __init__(self, dim1=1000, dim2=1000):
		self.grid = []
		for i in range(dim1):
			self.grid.append([])
			for j in range(dim2):
				self.grid[i].append(0)
	def getCount(self):
		return sum(sum(line) for line in self.grid)

	def runCommand(self, command, part):
		if ("turn" in command):
			start = command[2]
			end = command[4]
			if ("on" in command):
				self.alterRange(start, end, "on"+part)

			elif("off" in command):
				self.alterRange(start, end, "off"+part)

			else:
				print("Unkown command found in input data!")
				sys.exit(10)
		
		elif ("toggle" in command):
			start = command[1]
			end = command[3]
			self.alterRange(start, end, "toggle"+part)	
		
		else:
			print("Unkown command found in input data!")
			sys.exit(10)

	def alterRange(self, start, end, value):
		s = start.split(",")
		sx = int(s[0])
		sy = int(s[1])

		e = end.split(",")
		ex = int(e[0])
		ey = int(e[1])

		for y in range(sy, ey+1):
			for x in range(sx, ex+1):
				current = self.grid[y][x]
				if (value == "on1"):
					self.grid[y][x] = 1
				elif (value == "off1"):
					self.grid[y][x] = 0
				elif (value == "toggle1"):
					self.grid[y][x] = 1 - current
				elif (value == "on2"):
					self.grid[y][x] += 1
				elif (value == "off2"):
					if (current > 0):
						self.grid[y][x] -= 1
				elif (value == "toggle2"):
					self.grid[y][x] += 2
				else:
					print ("Value error in alterRange: " + value)
					sys.exit(101)

# ---

def resolve(lines, part):
	lg = LightGrid()
	commands = []
	for line in lines:
		commands.append(line.split(" "))
	iter = 1
	size = len(commands)
	for c in commands:
		print(str(iter) + "/" + str(size), end="\r")
		lg.runCommand(c, part)
		iter += 1
	print(str(iter-1) + "/" + str(size))
	return lg.getCount()