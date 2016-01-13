import re, random, copy

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

def listToMolecule(molList):
	return "".join(molList)
		
def calibrate(replacements, molecule):
	results = set() # Guarantee unique elements
	for rk in replacements.keys(): # for all atoms that can be replaced
		for r in replacements[rk]: # for all possible replacements for atom rk
			for i in range(len(molecule)): # for every atom in molecule
				if (molecule[i] == rk): # If current atom is replaceable
					new = copy.deepcopy(molecule)
					new[i] = r
					results.add(listToMolecule(new)) # Add molecule as string

	return len(results)

def reduce(mol, replacements, count=0):
	if (mol == 'e'):
		return count
	for rk in replacements.keys():
		indices = [m.start() for m in re.finditer(rk, mol)]
		for i in indices:
			for r in replacements[rk]:
				newMol = mol[:i]
				newMol += r
				newMol += mol[i+len(rk):]
				print(newMol)
				reduce(newMol, replacements, count+1)

def randomReduction(mol, replacements):
	options = []
	for rk in replacements.keys():
		indices = [m.start() for m in re.finditer(rk, mol)]
		for i in indices:
			options.append((i, rk, replacements[rk][0]))
	if (len(options) == 0):
		return None
	choice = random.choice(options)
	newMol = mol[:choice[0]]
	newMol += choice[2]
	newMol += mol[choice[0]+len(choice[1]):]
	return newMol

		

def reverseDict(d):
	inv = {}
	for k in d.keys():
		for v in d[k]:
			if v in inv.keys():
				inv[v].append(k)
			else:
				inv[v] = [k]
	return inv

# ---
def resolve(lines, part):
	replacements, molecule = parseLines(lines)
	reversedReplacements = reverseDict(replacements)

	
	if (part == '1'):
		return calibrate(replacements, molecule)
	else:
		molecule = listToMolecule(molecule)
		original = molecule

		while (True):
			count = 0
			while (molecule != 'e' and molecule != None):
				molecule = randomReduction(molecule, reversedReplacements)
				count += 1
			if (molecule == 'e'):
				return count
			else:
				molecule = original