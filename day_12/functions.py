import json

def countInCollection(c, illegalValue=None):
	if (type(c) == list):
		values = c
	elif (type(c) == dict):
		values = list(c.values())
		if (illegalValue in values):
			return 0
	else:
		throw(103)

	tot = 0
	for v in values:
		if (type(v) == int or type(v) == float):
				tot += v
		elif (type(v) == list):
			tot += countInCollection(v, illegalValue)
		elif (type(v) == dict):
			tot += countInCollection(v, illegalValue)

	return tot

# ---
def resolve(lines, part):

	line = lines[0].replace(" ", "")
	line = line.replace("\n", "")

	illegalValue = None
	if (part == '2'):
		illegalValue = "red"

	data = json.loads(line)
	result = countInCollection(data, illegalValue)
	return result