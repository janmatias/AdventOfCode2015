def iterateOverLine(line, part):
	floor = 0
	iteration = 0
	for c in line:
		iteration += 1
		if (c == '('):
			floor += 1
		elif (c == ')'):
			floor -= 1
		else:
			print ("Error in input data!")
			sys.exit(10)
		if (part == '2' and floor == -1):
			return iteration
	if (part == '2'):
		return -1
	return floor

# ---
def resolve(lines, part):
	line = lines[0]
	return iterateOverLine(line, part)