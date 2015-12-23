import math

def getPrimes(n):
	primes = []
	for i in range(2, n):
		for x in range(2, i):
			if i % x == 0:
				break
		else:
			primes.append(i)
	return primes

primes = [2]

def getNumberOfPresentsForHouse(house):
	num = 0
	"""
	steps = 1
	for p in primes:
		if (p >= house):
			break
		if (house % p != 0):
			steps *= p
	"""
	for i in range(1, int(math.sqrt(house)+2)):
		#print(i)
		if (house % i == 0):
			num += i*10
	return num

# ---
def resolve(lines, part):
	minPresents = int(lines[0])
	print("Min presents: " + str(minPresents))
	"""
	value = 0
	house = 0
	while (value < minPresents):
		house += 1
		value = 0
		for i in range(1, house+1):
			value += i * 10

	product = value
	print(house)
	for i in range(1, house+1):
		print(i)
		if (isPrime(i)):
			product *= i
	print(product)
	return
	print(getNumberOfPresentsForHouse(product))
	return product

	return house
	"""


	#print(getNumberOfPresentsForHouse(100000000))
	value = 0
	house = 100000
	while (value < minPresents):# and house < 10):
		house += 1
		value = getNumberOfPresentsForHouse(house)
		print(str(house) + ": " + str(minPresents - value))
	return house


