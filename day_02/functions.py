def parseDimensions(line):
	l, w, h = line.split('x')
	l = int(l)
	w = int(w)
	h = int(h)
	return l, w, h

def getFullArea(l, w, h):
	return 2*l*w + 2*w*h + 2*h*l

def getAreaOfSmallestSide(l, w, h):
	return min([l*w, l*h, w*h])

def getVolume(l, w, h):
	return l*w*h

def getLengthOfShortestPerimeter(l, w, h):
	sides = [l, w, h]
	del sides[sides.index(max(sides))]
	return sides[0]*2 + sides[1]*2

# ---
def resolve(lines, part):
	total = 0
	for line in lines:
		l, w, h = parseDimensions(line)
		if (part == '1'):
			total += getFullArea(l, w, h) + getAreaOfSmallestSide(l, w, h)
		elif(part == '2'):
			total += getLengthOfShortestPerimeter(l, w, h) + getVolume(l, w, h)
	return total
