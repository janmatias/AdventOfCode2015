import copy, random, sys

def startTurn(mana, armor, BossHP, activeEffects):
	toDel = []
	for name, values in activeEffects.items():
		if (name == "Recharge"):
			mana += values["mana"]
			values["turns"] -= 1
			print("Recharge provides %s mana; its timer is now %s." % (values["mana"], values["turns"]))
			if (values["turns"] == 0):
				print("Recharge wears off.")
				toDel.append("Recharge")
		elif (name == "Shield"):
			values["turns"] -= 1
			print("Shields timer is now %s." % values["turns"])
			if (values["turns"] == 0):
				armor = 0
				print("Shield wears off, decreasing armor by %s." % values["armor"])
				toDel.append("Shield")
		elif (name == "Poison"):
			BossHP -= values["damage"]
			values["turns"] -= 1
			print("Poison deals %s damage; its timer is now %s." % (values["damage"], values["turns"]))
			if (values["turns"] == 0):
				print("Poison wears off.")
				toDel.append("Poison")

		else:
			print("IllegalEffectInActiveEffects")

	for d in toDel:
		del activeEffects[d]

	return mana, armor, BossHP, activeEffects

def chooseSpell(armor, HP, BossHP, BossDmg, mana, spells, activeEffects):
	choice = random.choice([x for x in spells.keys() if (x not in activeEffects.keys() and spells[x]["cost"] <= mana)])
	return choice, spells[choice]["cost"]

def castSpell(spell, spells, activeEffects, HP, armor, BossHP):
	if (spell == "Drain"):
		HP += spells["Drain"]["heal"]
		BossHP -= spells["Drain"]["damage"]
	elif (spell == "Magic Missile"):
		BossHP -= spells["Magic Missile"]["damage"]
	else:
		if(spell in activeEffects.keys()):
			SpellAlreadyCast
		if (spell == "Shield"):
			armor = spells["Shield"]["armor"]
		activeEffects[spell] = copy.deepcopy(spells[spell])
	return activeEffects, HP, armor, BossHP

# Disable print
def print(string):
	pass

# ---
def resolve(lines, part):
	# Format: name, 			cost, 	turns, 	damage, heal, 	armor, 	mana

	spells = {"Magic Missile" : {"cost" :  53, "turns" : 0, "damage" : 4, "heal" : 0, "armor" : 0, "mana" : 0},
			  "Drain" : 		{"cost" :  73, "turns" : 0, "damage" : 2, "heal" : 2, "armor" : 0, "mana" : 0},
			  "Shield" : 		{"cost" : 113, "turns" : 6, "damage" : 0, "heal" : 0, "armor" : 7, "mana" : 0},
			  "Poison" : 		{"cost" : 173, "turns" : 6, "damage" : 3, "heal" : 0, "armor" : 0, "mana" : 0},
			  "Recharge" : 		{"cost" : 229, "turns" : 5, "damage" : 0, "heal" : 0, "armor" : 0, "mana" : 101},
			 }

	outputs = []
	minMana = sys.maxsize
	for i in range(100000):

		BossHP = int(lines[0].split(" ")[-1])
		BossDmg = int(lines[1].split(" ")[-1])

		mana = 500
		HP = 50
		armor = 0
		activeEffects = {}
		manaSpent = 0
		output = "Victory!"
		while(HP > 0 and BossHP > 0):

			print("\n-- Player Turn --")
			print("- Player has %s hit points, %s armor, %s mana" % (HP, armor, mana))
			print("- Boss has %s hit points" % BossHP)

			if (part == '2'):
				HP -= 1
				if (HP <= 0):
					break

			mana, armor, BossHP, activeEffects = startTurn(mana, armor, BossHP, activeEffects)

			if (mana < 53):
				output = "No more mana for spells"
				break

			toCast, cost = chooseSpell(armor, HP, BossHP, BossDmg, mana, spells, activeEffects)

			print("Player casts %s for %s mana." % (toCast, cost))

			manaSpent += cost
			if (mana < cost):
				output = "Mana error"
				break
			mana -= cost
			activeEffects, HP, armor, BossHP = castSpell(toCast, spells, activeEffects, HP, armor, BossHP)
			if (BossHP <= 0):
				break
			
			print("\n-- Boss Turn --")
			print("- Player has %s hit points, %s armor, %s mana" % (HP, armor, mana))
			print("- Boss has %s hit points" % BossHP)

			mana, armor, BossHP, activeEffects = startTurn(mana, armor, BossHP, activeEffects)
			if (BossHP <= 0):
				break
			HP -= max(BossDmg - armor, 1)
			print("Boss attacks for %s damage." % max(BossDmg - armor, 1))

		if (HP <= 0 or output == "No more mana for spells"):
			continue
		else:
			print(manaSpent)
			print("")
			minMana = min(minMana, manaSpent)
		outputs.append(output)

	print(outputs)
	return minMana
