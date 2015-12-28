import copy
from day_19.CustomAStar.CustomSolver import CustomSolver

def parseLines(lines):
	molecule = ""
	replacements = {}
	for line in lines:
		split = line.split(" ")
		if (len(split) == 1): # Then line is molecule
			molecule = moleculeToList(line)
		else: # Then line is a replacement
			fm = split[0]
			tm = split[2]
			if (fm in replacements.keys()):
				replacements[fm].append(tm)
			else:
				replacements[fm] = [tm]
	return replacements, molecule

def moleculeToList(molecule):
	atoms = []
	previousTwoLetter = False
	for i in range(len(molecule)-1):
		if(previousTwoLetter):
			previousTwoLetter = False
			continue
		if (molecule[i+1].isupper()):
			atoms.append(molecule[i])
		else:
			atoms.append(molecule[i:i+2])
			previousTwoLetter = True
	if (molecule[-1].isupper()):
		atoms.append(molecule[-1])

	return atoms
		
def calibrate(replacements, molecule):
	results = set() # Guarantee unique elements
	for rk in replacements.keys(): # for all atoms that can be replaced
		for r in replacements[rk]: # for all possible replacements for atom rk
			for i in range(len(molecule)): # for every atom in molecule
				if (molecule[i] == rk):
					new = copy.deepcopy(molecule)
					new[i] = r
					results.add("".join(new)) # Add molecule as string

	return len(results)

def create(replacements, molecule):
	possibleOuts = [['e']]
	count = 0
	while (molecule not in possibleOuts):
		#print(possibleOuts)
		count += 1
		if (count == 10):
			thr
		current = copy.deepcopy(possibleOuts)
		possibleOuts = []
		for rk in replacements.keys():
			for r in replacements[rk]:
				for c in current:
					for i in range(len(c)):
						if (c[i] == rk):
							new = copy.deepcopy(c)
							insertion = moleculeToList(r)
							ic = 0
							for ai in range(len(insertion)):
								new.insert(i + ic, insertion[ai])
								ic += 1
							
							possibleOuts.append(new)
							
	return count


# ---
def resolve(lines, part):
	replacements, molecule = parseLines(lines)

	if (part == '1'):
		return calibrate(replacements, molecule)
	else:
		solver = CustomSolver("".join(molecule), replacements)
		result = solver.search()
		return result
		#backwards(replacements, "".join(molecule))
		#return create(replacements, molecule)


	
	
