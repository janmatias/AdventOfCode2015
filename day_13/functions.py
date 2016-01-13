import itertools, sys

def calculateHappiness(people, permutation, verbose=False):
	h = 0
	# Check happiness for both neighbours
	for i in range(len(permutation)):
		h += people[permutation[i]][permutation[i-1]]
		h += people[permutation[i]][permutation[(i+1)%len(permutation)]] # %: used for simulating round table (the last person sits next to the first)

	if (verbose):
		print(permutation)
		for i in range(len(permutation)):
			if (i == len(permutation)-1):
				print (permutation[i] + " - n1: " + permutation[i-1] + " - n2: " + permutation[0])
				print("Added: " + str(people[permutation[i]][permutation[i-1]]))
				print("Added: " + str(people[permutation[i]][permutation[0]]))
			else:
				print (permutation[i] + " - n1: " + permutation[i-1] + " - n2: " + permutation[i+1])
				print("Added: " + str(people[permutation[i]][permutation[i-1]]))
				print("Added: " + str(people[permutation[i]][permutation[i+1]]))
		
	return h

# ---
def resolve(lines, part):
	# Generate dictionary containing every person
	people = {}
	for line in lines:
		l = line.split(" ")
		p1 = l[0]
		p2 = l[-1][:-1]
		if (l[2] == "gain"):
			h = int(l[3])
		else:
			h = -int(l[3])
		if (p1 not in people.keys()):
			people[p1] = {p2 : h}
		else:
			people[p1][p2] = h

	# Add oneself to the list of people
	if (part == '2'):
		people["you"] = {}
		for k in people.keys():
			if (k == "you"):
				pass
			else:
				people["you"][k] = 0
				people[k]["you"] = 0

	# Find permutation with highest happiness
	optimal = -sys.maxsize
	for p in itertools.permutations(list(people.keys())):
		optimal = max(calculateHappiness(people, p), optimal)
	
	return optimal