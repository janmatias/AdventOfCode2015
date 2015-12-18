import itertools

# ---
def resolve(lines, part):
	eggnog = 150 # Amiunt of liquid to contain
	containers = []

	for line in lines:
		containers.append(int(line))

	possibilities = 0
	minNumberOfContainers = len(containers)
	for i in range(len(containers)):
		minSum = 0
		for comb in itertools.combinations(containers, i):
			s = sum(comb)
			minSum = min(s, minSum)
			if (s == eggnog):
				minNumberOfContainers = min(minNumberOfContainers, len(comb))
				possibilities += 1
		if (minSum > eggnog): # If sum minimum combination is greater than eggnog, there is no point in trying larger combinations
			break

	if (part == '2'):
		possibilities = 0
		for comb in itertools.combinations(containers, minNumberOfContainers):
			if (sum(comb) == eggnog):
				possibilities += 1

	return possibilities