def lookAndSay(s):
	cc = None # cc - current character
	count = 1
	newS = ""
	for c in s:
		if (c == cc):
			count += 1
		else:
			if (cc is not None):
				newS += str(count) + cc
			cc = c
			count = 1
	if (cc is not None):
		newS += str(count) + cc
	return newS

# ---
def resolve(lines, part):

	if (part == '2'):
		iterations = 50
	else:
		iterations = 40

	result = ""
	for line in lines:
		for _ in range(iterations):
			line = lookAndSay(line)
		result += str(len(line)) + "\n"
	return result[:-1]


