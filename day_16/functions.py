def parseLines(lines):
	aunts = []

	for line in lines:
		aunt = {}
		splitLine = line.split(" ")
		index = 3

		while (index < len(splitLine)):
			compund = splitLine[index-1][:-1]
			value = splitLine[index]
			if (value[-1] == ','):
				value = value[:-1]
			value = int(value)
			aunt[compund] = value
			index += 2

		aunts.append(aunt)

	return aunts

# ---
def resolve(lines, part):

	aunts = parseLines(lines)

	MFCSAM = {	"children" : 3,
				"cats" : 7,
				"samoyeds" : 2,
				"pomeranians" : 3,
				"akitas" : 0,
				"vizslas" : 0,
				"goldfish" : 5,
				"trees" : 3,
				"cars" : 2,
				"perfumes" : 1}

	gtKeys = ["cats", "trees"] # indicates that value must be greater for these keys
	ltKeys = ["pomeranians", "goldfish"] # indicates that value must be less for these keys

	i = 0
	for aunt in aunts:
		i += 1
		numCorrect = 0

		for k, v in aunt.items():
			if (part == '1' and MFCSAM[k] == v):
				numCorrect += 1
			elif (part == '2'):
				if (k in gtKeys):
					if (MFCSAM[k] < v):
						numCorrect += 1
				elif (k in ltKeys):
					if (MFCSAM[k] > v):
						numCorrect += 1
				else:
					if (MFCSAM[k] == v):
						numCorrect += 1

		if (numCorrect == 3):
			break
			
	return i