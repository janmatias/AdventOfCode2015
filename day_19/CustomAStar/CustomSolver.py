from day_19.GeneralAStar.GeneralSolver import GeneralSolver
from day_19.CustomAStar.CustomSearchNode import CustomSearchNode
from day_19.CustomAStar.CustomState import CustomState

class CustomSolver(GeneralSolver):
    def __init__(self, initialMolecule, replacements):
        self.initialMolecule = initialMolecule
        self.replacements = replacements
        GeneralSolver.__init__(self)

    def genInitialNode(self):
        self.currentSearchNode = CustomSearchNode(CustomState(self.initialMolecule, self.replacements))
        return self.currentSearchNode

    def arcCost(self, node1, node2):
        return abs(node1.state.numReplacements - node2.state.numReplacements)

