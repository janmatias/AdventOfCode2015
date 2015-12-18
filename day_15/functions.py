def score(ingredients, amounts):
	totals = [0, 0, 0, 0] # Hardcoded :/
	length = len(totals)
	
	for i in range(length):
		for j in range(length):
			totals[j] += amounts[i] * ingredients[i][j]
	
	product = 1
	for i in range(len(totals)):
		if (totals[i] < 0):
			totals[i] = 0
		product *= totals[i]

	return product

def numCalories(ingredients, amounts):
	calories = 0
	length = len(ingredients)
	if (length != len(amounts)):
		throw(104)
	for i in range(length):
		calories += amounts[i] * ingredients[i][4]
	
	return calories

def parseLines(lines):
	ingredients = []

	for line in lines:
		splitline = line.split(" ")
		ingredient = []
		ingredient.append(int(splitline[2][:-1]))
		ingredient.append(int(splitline[4][:-1]))
		ingredient.append(int(splitline[6][:-1]))
		ingredient.append(int(splitline[8][:-1]))
		ingredient.append(int(splitline[10]))

		ingredients.append(ingredient)

	return ingredients

# ---
def resolve(lines, part):
	ingredients = parseLines(lines)
	
	maxScore = -1
	# 101 used in the for loops, as ranges are not inclusive of their end value
	# The for loops are unfortunately hard coded for this problem :/
	for i1 in range(1, 101):
		for i2 in range(1, 101-i1):
			for i3 in range(1, 101-i1-i2):
				i4 = 100-i1-i2-i3 # 100 is used, as this is not a range
				if (part == '2' and numCalories(ingredients, [i1, i2, i3, i4]) != 500):
					continue
				s = score(ingredients, [i1, i2, i3, i4])
				if (s > maxScore):
					maxScore = s
					best = [i1, i2, i3, i4]

	return maxScore