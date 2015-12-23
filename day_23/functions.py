def parseInput(lines):
	commands = []
	for line in lines:
		split = line.split(" ")
		if (split[0] == "jio" or split[0] == "jie"):
			commands.append([split[0], parseRegsister(split[1]), parseInt(split[2])])
		elif(split[0] != "jmp"):
			commands.append([split[0], parseRegsister(split[1])])
		else:
			commands.append([split[0], parseInt(split[1])])
	return commands

def parseInt(string):
	if (string[0] == "-"):
		return -int(string[1:])
	elif(string[0] == "+"):
		return int(string[1:])
	else:
		return "-1"

def parseRegsister(reg):
	if (reg[0] == "a"):
		return 0
	elif(reg[0] == "b"):
		return 1
	else:
		return -1

def runCommand(command, registers):
	nextCommand = 1
	if (command[0] == "hlf"):
		registers[command[1]] = int(registers[command[1]]/2)
	elif (command[0] == "tpl"):
		registers[command[1]] *= 3
	elif (command[0] == "inc"):
		registers[command[1]] += 1
	elif (command[0] == "jmp"):
		nextCommand = command[1]
	elif (command[0] == "jie"):
		if (registers[command[1]] % 2 == 0):
			nextCommand = command[2]
	elif (command[0] == "jio"):
		if (registers[command[1]] == 1):
			nextCommand = command[2]
	else:
		return ""	
	return registers, nextCommand
	
# ---
def resolve(lines, part):
	commands = parseInput(lines)
	
	registers = [0,0]
	if (part == '2'):
		registers[0] = 1

	pc = 0
	while (pc < len(commands)):
		registers, next = runCommand(commands[pc], registers)
		pc += next

	return registers[1]
