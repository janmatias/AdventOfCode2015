import operator

class Wire():
	def __init__(self, identifier, unparsedInput=None, value=None):
		self.identifier = identifier
		self.unparsedInput = unparsedInput
		self.value = value



class Circuit():
	def __init__(self):
		self.wires = {}

	def addWire(self, line):
		input, output = line.split(" -> ")
		self.wires[output] = Wire(output, input)

	def getValueForWire(self, WID):
		if (WID in self.wires.keys() and self.wires[WID].value is not None):
			return self.wires[WID].value
		else:
			self.wires[WID].value = self.parse(self.wires[WID].unparsedInput)
			return self.wires[WID].value

	def parse(self, input):
		input = input.split(" ")
		if (len(input) == 1):
			if (input[0].isdigit()):
				return int(input[0])
			else:
				return self.getValueForWire(input[0])
		elif (len(input) == 2):
			if (input[0] != 'NOT'):
				throw(110)
			return ~self.parse(input[1])
		elif (len(input) == 3):
			v1 = self.parse(input[0])
			v2 = self.parse(input[2])
			op = None
			if (input[1] == 'AND'):
				op = operator.and_
			elif (input[1] == 'OR'):
				op = operator.or_
			elif (input[1] == 'RSHIFT'):
				op = operator.rshift
			elif (input[1] == 'LSHIFT'):
				op = operator.lshift
			else:
				throw(110)
			return op(v1, v2)

		else:
			throw(110)

# ---
def resolve(lines, part):

	circuit = Circuit()
	for line in lines:
		line.replace("\n", "")
		circuit.addWire(line)
	if (part == '1'):
		return circuit.getValueForWire('a')
	elif (part == '2'):
		sa = str(circuit.getValueForWire('a'))
		for wire in circuit.wires.values():
			wire.value = None
		circuit.wires['b'].value = int(sa)
		return circuit.getValueForWire('a')

	else:
		throw(110)

