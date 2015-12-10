v = False

def doSomethingFancy(line):
	pass

# ---
def resolve(lines, part, verbose=False):
	v = verbose

	result = 0
	for line in lines:
		line = line.replace("\n", "")

		result += doSomethingFancy(line)

	return result
