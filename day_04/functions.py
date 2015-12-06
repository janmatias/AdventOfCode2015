from hashlib import md5


# ---
def resolve(lines, part):
	data = lines[0]
	target = "00000"
	if (part == '2'):
		target += '0'
	iteration = -1
	while True:
		iteration += 1
		s = (data+str(iteration)).encode('utf-8')
		m = md5()
		m.update(s)
		h = m.hexdigest()

		if (h[:len(target)] == target):
			return iteration