import sys, os.path, argparse
from errorHandling.handler import *

parser = argparse.ArgumentParser(description="This program is able to run the adventofcode solutions.")

parser.add_argument('day', type=int, choices=[x for x in range(1, 26)], help="Varible to define what day to run.")
parser.add_argument('part', nargs='?', const='1', default='1', choices=['1', '2'], help="Variable to define what part of the challenge to solve.")
parser.add_argument('-t', '--testing', action='store_true', help="Boolean to set the test data file as the input.")

args = parser.parse_args()

# Import correct day
dayList = ["day_0"+str(x) for x in range(1, 10)]
dayList.extend(["day_"+str(x) for x in range(10, 25)])

package = dayList[int(args.day)-1]
module = __import__(package + '.functions', fromlist=["resolve"])
resolve = getattr(module, "resolve")

dataFilePath = None
# Find data file
if (args.testing):
	dataFilePath = package + "/test.txt"
	if (not os.path.isfile(dataFilePath)):
		throw(3)
elif (os.path.isfile(package + "/data.txt")):
	dataFilePath = package + "/data.txt"
elif (os.path.isfile(package + "/input.txt")):
	dataFilePath = package + "/input.txt"
else:
	throw(11)

# Load data
lines = []
data = open(dataFilePath, "r")
for line in data:
	line = line.replace("\n", "")
	lines.append(line)
data.close()

# Execute main program
result = resolve(lines, args.part)
print ("Result: " + str(result))