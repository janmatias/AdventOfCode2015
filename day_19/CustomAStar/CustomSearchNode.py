import copy

from day_19.GeneralAStar.GeneralSearchNode import GeneralSearchNode
from day_19.CustomAStar.CustomState import CustomState


class CustomSearchNode(GeneralSearchNode):
    def __init__(self, state, g = 0, parent = None):
        GeneralSearchNode.__init__(self, state)

    def _h(self):
        return len(self.state.molecule)/6.0

    def isSolution(self):
        return self.state.molecule == 'e'

    def genAllSuccessors(self):
        arr = []
        for n in self._possibleSuccessors():
            node = CustomSearchNode(n)
            arr.append(node)
        print("arr: " + str(arr))
        return arr

    def _possibleSuccessors(self):
        states = []
        for rep in self.state.sortedReplacements:
            print(rep)
            print(self.state.molecule)
            if (rep in self.state.molecule):
                newState = copy.deepcopy(self.state)
                newState.numReplacements += 1
                newState.molecule = newState.molecule.replace(rep, self.state.backRep[rep][0], 1)
                states.append(newState)
        print("states: " + str(states))
        return states



"""
def backwards(replacements, molecule):
    m = "".join(molecule)
    backRep = {}
    #print(replacements)
    for k, v in replacements.items():
        for value in v:
            if (value in backRep.keys()):
                backRep[value].append(k)
            else:
                backRep[value] = [k]
    #print(backRep)

    sortedReps = list(reversed(sorted(list(backRep.keys()), key=len)))
    print(sortedReps)


    while (molecule != 'e'):
        noReplacements = True
        for i in range(len(sortedReps)):
            current = sortedReps[i]
            if (current in molecule):
                noReplacements = False
                print(molecule)
                molecule = molecule.replace(current, backRep[current][0], 1)
                print(molecule)
                break
        if (noReplacements):
            print("noReplacements")
            break

        
        

    print(sortedReps)
    """