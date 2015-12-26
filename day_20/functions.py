def deliverPresentsUpToHouses(limit, part):
	houses = [0] * limit

	for elf in range(1, limit):
		delivered = 0
		for elfDeliveries in range(elf, limit, elf): # deliver present for each elf elf
			if (part == '1'):
				houses[elfDeliveries] += elf*10
			elif (delivered < 50):
				houses[elfDeliveries] += elf*11
				delivered += 1
	return houses

#-- 
def resolve(lines, part):
	target = int(lines[0])
	
	houses = deliverPresentsUpToHouses(1000000, part)
	
	# Find first house to hit (or pass) target
	for i in range(len(houses)):
		if (houses[i] >= target):
			return i

	# If no house found, return illegal value (-1)
	return -1