import sys
from functions import *

# Options
allConfigurations = ['1', '2']

### -Run
# Load data
lines = []
data = open("data.txt", "r")
for line in data:
	line = line.replace("\n", "")
	lines.append(line)
data.close()

# Check command line arguments
if (len(sys.argv) == 1):
	part = '1'
elif (len(sys.argv) == 2):
	if (sys.argv[1] in allConfigurations):
		part = sys.argv[1]
	else:
		print("Illegal parameter!\nLegal parameters are: " + str(allConfigurations))
		sys.exit(1)
else:
	print("Illegal number of parameters!" + str(allConfigurations))
	sys.exit(2)

# Execute main program
result = resolve(lines, part)

print ("Result: " + str(result))