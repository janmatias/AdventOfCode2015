def getVowelCount(string):
	count = 0
	for c in string:
		if (c in "aeiou"):
			count += 1
	return count

def containsDoubleLetter(string):
	prev = None
	for c in string:
		if prev is None:
			prev = c
			continue
		elif (c == prev):
			return True
		prev = c
	return False

def containsEqualsSeparatedByAtLeastOne(string):
	for i in range(2, len(string)):
		if (string[i] == string[i-2]):
			return True
	return False
		
def containsMultiplesOfAnyPair(string):
	for i in range(len(string)-1):
		if (string.count(string[i] + string[i+1]) > 1):
			return True
	return False

def stringIsNiceV1(string):
	if ("ab" in string or "cd" in string or "pq" in string or "xy" in string):
		return 0
	if ((getVowelCount(string) >= 3) and containsDoubleLetter(string)):
		return 1
	return 0

def stringIsNiceV2(string):
	if (containsEqualsSeparatedByAtLeastOne(string) and containsMultiplesOfAnyPair(string)):		
		return 1
	return 0

# ---

def resolve(lines, part):
	result = 0
	for line in lines:
		if (part == '1'):
			result += stringIsNiceV1(line)
		elif (part == '2'):
			result += stringIsNiceV2(line)
		else:
			print ("Something went wrong internally!\nPart variable has illegal value in resolve.")
			sys.exit(100)
	return result