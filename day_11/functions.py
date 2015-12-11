v = False
alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
illegal = [8, 11, 14]

def convertPasswordToPassList(password):
	l = []
	for c in password:
		if (c not in alfabet):
			throw(10)
		l.append(alfabet.index(c))
	return l

def convertPassListToPassword(l):
	s = ""
	for i in l:
		s += alfabet[i]
	return s

def incrementPassList(passList):
	index = -1
	for i in range(-len(passList), 0):
		if passList[i] in illegal:
			index = i
			if (v): 
				print("Illegal character found at: " + str(i))
			for j in range(i+1, 0):
				passList[j] = 0
	while (abs(index) <= len(passList)):
		passList[index] += 1
		if (passList[index] >= len(alfabet)):
			passList[index] = 0
			index -= 1
		else:
			index = len(alfabet)

def containsThreeConsecutiveIncreasingCharacters(passList):
	for i in range(len(passList)-2):
		if (passList[i] == passList[i+1] - 1 and passList[i] == passList[i+2] - 2):
			return True
	return False

def containsIllegalCharacter(passList):
	return [c for c in passList if c in illegal]

def containsTwoDifferentPairs(passList):
	foundOnePair = False
	foundLastITeration = False
	foundPairCaracter = ""
	for i in range(len(passList)-1):
		if (foundLastITeration):
			foundLastITeration = False
			continue
		if (passList[i] == passList[i+1]):
			if (foundOnePair and foundPairCaracter != passList[i]):
				return True
			else:
				foundPairCaracter = passList[i]
				foundLastITeration = True
				foundOnePair = True
	return False


def passListIsLegal(passList):
	return containsThreeConsecutiveIncreasingCharacters(passList) and not containsIllegalCharacter(passList) and containsTwoDifferentPairs(passList)

# ---
def resolve(lines, part, verbose=True):
	v = verbose
	result = ""
	for line in lines:
		line = line.replace("\n", "")
		passList = convertPasswordToPassList(line)

		while (not passListIsLegal(passList)):
			incrementPassList(passList)
		
		result += convertPassListToPassword(passList)  + '\n'

		#result += doSomethingFancy(line) + "\n"

	return result[:-1]
