from day_19.GeneralAStar.GeneralState import GeneralState


class CustomState(GeneralState):
    def __init__(self, molecule, replacements):
        self.molecule = molecule
        self.numReplacements = 0
        self.backRep = {}
        #print(replacements)
        for k, v in replacements.items():
            for value in v:
                if (value in self.backRep.keys()):
                    self.backRep[value].append(k)
                else:
                    self.backRep[value] = [k]

        self.sortedReplacements = list(reversed(sorted(list(self.backRep.keys()), key=len)))

        GeneralState.__init__(self)

    def genUniqueID(self):
        return self.molecule