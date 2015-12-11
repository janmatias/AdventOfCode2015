class Password():
	dAlfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	dIllegal = ['i', 'l', 'o']
	def __init__(self, string, alfabet=dAlfabet, illegal=dIllegal):
		self.passwd = string
		self.alfabet = alfabet
		self.alfabetLength = len(alfabet)
		self.illegal = [alfabet.index(c) for c in alfabet if c in illegal]
		self.convertPasswordToPassList()

	def toString(self):
		return str(self.passwd)

	def setPassword(self, newPassword):
		self.passwd = newPassword
		self.convertPasswordToPassList()

	def convertPasswordToPassList(self):
		self.passList = []
		for c in self.passwd:
			if (c not in self.alfabet):
				throw(10)
			self.passList.append(self.alfabet.index(c))
		self.passListLength = len(self.passList)

	def convertPassListToPassword(self):
		self.passwd = ""
		for i in self.passList:
			self.passwd += self.alfabet[i]

	def incrementPassList(self):
		index = -1
		for i in range(-self.passListLength, 0):
			if self.passList[i] in self.illegal:
				index = i
				for j in range(i+1, 0):
					self.passList[j] = 0
		while (abs(index) <= self.passListLength):
			#print(index)
			self.passList[index] += 1
			if (self.passList[index] >= self.alfabetLength):
				self.passList[index] = 0
				index -= 1
			else:
				index = -self.passListLength

	def containsThreeConsecutiveIncreasingCharacters(self):
		for i in range(self.passListLength-2):
			if (self.passList[i] == self.passList[i+1] - 1 and self.passList[i] == self.passList[i+2] - 2):
				return True
		return False

	def containsIllegalCharacter(self):
		return [c for c in self.passList if c in self.illegal]

	def containsTwoDifferentPairs(self):
		foundOnePair = False
		foundLastITeration = False
		foundPairCaracter = ""
		for i in range(self.passListLength-1):
			if (foundLastITeration):
				foundLastITeration = False
				continue
			if (self.passList[i] == self.passList[i+1]):
				if (foundOnePair and foundPairCaracter != self.passList[i]):
					return True
				else:
					foundPairCaracter = self.passList[i]
					foundLastITeration = True
					foundOnePair = True
		return False

	def findNextLegalPass(self):
		self.incrementPassList()
		while (not self.passListIsLegal()):
			self.incrementPassList()
		self.convertPassListToPassword()

	# Override this methid in subclass to update password rules
	def passListIsLegal(self):
		return (self.containsThreeConsecutiveIncreasingCharacters() 
			and self.containsTwoDifferentPairs()
			and not self.containsIllegalCharacter())

# ---
def resolve(lines, part):
	passwd = Password("")
	result = ""
	for line in lines:
		line = line.replace("\n", "")
		print("original: " + line)
		passwd.setPassword(line)
		passwd.findNextLegalPass()
		result += passwd.toString() + "\n"
		if (part == '2'):
			passwd.findNextLegalPass()
			result += passwd.toString() + "\n"
		print("----------------")

	return result[:-1]
