def getMemorySize(string):
	size = 0
	i = 1
	prevWasBack = False
	while i < len(string)-1:
		c = string[i]
		if (prevWasBack):
			prevWasBack = False
			if (c == 'x'):
				i += 2 # skip two digit 'id' hexadecimals; "\xid"
				size += 1 # This is replaced by single character; "\x26" --> "'"
			elif (c == '\\' or c == '\"'):
				size += 1
			else:
				throw(10)
		else:
			if (c == "\\"):
				prevWasBack = True
			else:
				size += 1

		i += 1
	return size

def encode(string):
	encoded = '"'
	for c in string:
		if (c == '"'):
			encoded += '\\"' # --> \"
		elif (c == '\\'):
			encoded += '\\\\' # --> \\
		else:
			encoded += c
	encoded += '"'
	return encoded

# ---
def resolve(lines, part, verbose=False):
	sumLiterals = 0
	sumMemory = 0
	sumEncoded = 0
	for line in lines:
		sumLiterals += len(line)
		sumMemory += getMemorySize(line)
		sumEncoded += len(encode(line))

	if (part == '1'):
		return sumLiterals - sumMemory
	elif (part == '2'):
		return sumEncoded - sumLiterals
	else:
		throw(110)