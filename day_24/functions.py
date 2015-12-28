import itertools

def prod(l): # same as sum(), but for product
	product = 1
	for x in l:
		product *= x
	return product

def parseInput(lines):
	packages = []
	for line in lines:
		packages.append(int(line))
	return packages

def canSplit(l, groups, groupSum): # Recursive check for legal split of list
	if (groups == 1 and sum(l) == groupSum):
		return True
	else:
		for i in range(len(l)):
			for c in itertools.combinations(l, i):
				if (sum(c) == groupSum and canSplit([x for x in l if x not in c], groups-1, groupSum)):
					return True
		return False

# ---
def resolve(lines, part):
	packages = parseInput(lines)
	groupSum = sum(packages)/(int(part)+2) # Problem specific variable. (part 1: 3; part 2: 4)

	# Returning the first valid result from itertools.combinations works with sorted input as the combination s will be sorted too.
	for i in range(1, len(packages)):
		for c in itertools.combinations(packages, i):
			if (sum(c) == groupSum and canSplit([x for x in packages if x not in c], (int(part)+1), groupSum)):
				return prod(c)

	return False