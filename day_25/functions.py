def parseInput(lines):
	col = int(lines[0].split(" ")[-1][:-1])
	row = int(lines[0].split(" ")[-3][:-1])
	return (row,col)

# ---
def resolve(lines, part):

	row, col = parseInput(lines)

	iterations = (row-1) * (col-1) # square: 0 -> row-1 and 0-> col-1
	iterations += ((col)**2 + (col)) / 2 # First triangle
	iterations += ((row-1)**2 + (row-1)) / 2 # Second triangle

	number = 20151125
	for i in range(int(iterations-1)):
		number = (number * 252533) % 33554393

	return number