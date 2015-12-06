import sys
from errorHandling.handler import *

# Options
day = '1'
part = '1'
partsForDay = [['1', '2'] for x in range(24)]
days = [str(x) for x in range(1,25)]

# Check command line arguments to initiate correct day
if (len(sys.argv) == 2):
	if (sys.argv[1] in days):
		day = sys.argv[1]
	else:
		throw(1)
elif (len(sys.argv) == 3):
	if (sys.argv[1] in days and sys.argv[2] in partsForDay[int(sys.argv[1])-1]):
		day = sys.argv[1]
		part = sys.argv[2]
	else:
		throw(1)
else:
	throw(2)

# Import correct day
l = ["day_0"+str(x) for x in range(1, 10)]
l.extend(["day_"+str(x) for x in range(10, 25)])

package = l[int(day)-1]
module = __import__(package + '.functions', fromlist=["resolve"])
resolve = getattr(module, "resolve")

# Load data
lines = []
data = open(package + "/data.txt", "r")
for line in data:
	line = line.replace("\n", "")
	lines.append(line)
data.close()

# Execute main program
result = resolve(lines, part)
print ("Result: " + str(result))