import copy

def newGrid():
	return [[0 for _ in range(gridSizeX)] for _ in range(gridSizeY)]

def parseLines(lines):
	grid = newGrid()

	x, y = -1, -1
	for line in lines:
		y += 1
		x = -1
		for c in line:
			x += 1
			if (c == '#'):
				grid[y][x] = 1

	return grid

def nextValue(grid, x, y):
	neighboursOn = 0
	neighbourIndices = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

	for ny, nx in neighbourIndices:
		if (y + ny < 0 or x + nx < 0 or y + ny >= len(grid) or x + nx >= len(grid[y])): # Check bounds
			continue
		if (grid[y+ny][x+nx]):
			neighboursOn += 1
		
	if (grid[y][x] == 0): # If off
		if (neighboursOn == 3):
			return 1
		return 0
	else: # if on
		if (neighboursOn == 2 or neighboursOn == 3):
			return 1
		return 0

def setCornersOn(grid):
	grid[0][0] = 1
	grid[0][len(grid[0])-1] = 1
	grid[len(grid)-1][0] = 1
	grid[len(grid)-1][len(grid[-1])-1] = 1

def printGrid(grid):
	print("----------")
	for line in grid:
		print(line)
	print("----------")

# ---
gridSizeX, gridSizeY = 100, 100 # Edit to 6, 6 for test case
def resolve(lines, part):
	grid = parseLines(lines)
	numIterations = 100 # Edit to 4(or 5) for test case

	for i in range(numIterations):
		if (part == '2'):
			setCornersOn(grid)

		next = copy.deepcopy(grid)
		for y in range(gridSizeY):
			for x in range(gridSizeX):
				next[y][x] = nextValue(grid, x, y)
		grid = next

	if (part == '2'):
		setCornersOn(grid)
	#printGrid(grid)
				
	return sum(sum(grid[i]) for i in range(len(grid)))
