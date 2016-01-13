import itertools, sys

def parseInput(lines):
	if (len(lines) != 3):
		return
	return (int(lines[x].split(" ")[-1]) for x in range(3))

# ---
def resolve(lines, part):

	# HP is irrelevant for this problem, as damage is static after item purchases.
	_, Bdmg, Barmor = parseInput(lines) # 100, 8, 2

	# hardcoded, pls fix
	dmg, armor = 0, 0

	# hardcoded, pls fix
	weapons = ((4,8), (5,10), (6,25), (7,40), (8,74))
	armors = ((0,0), (1,13), (2,31), (3,53), (4,75), (5,102))
	rings = ((0,0), (0,0), (1,25), (2,50), (3,100), (-1,20), (-2,40), (-3,80))

	minCost = sys.maxsize
	maxCost = -1
	for w in weapons:
		for a in armors:
			for rc in itertools.combinations(rings, 2):
				dmg = w[0]
				cost = w[1]
				armor = a[0]
				cost += a[1]
				for r in rc:
					if (r[0] < 0):
						armor += abs(r[0])
						cost += r[1]
					elif (r[0] > 0):
						dmg += r[0]
						cost += r[1]

				damageDealt = max(dmg - Barmor, 1)
				damageTaken = max(Bdmg - armor, 1)

				if (damageDealt >= damageTaken and cost < minCost):
					minCost = cost
				if (damageDealt < damageTaken and cost > maxCost):
					maxCost = cost

	if (part == '1'):
		return minCost
	elif (part == '2'):
		return maxCost
	return False
