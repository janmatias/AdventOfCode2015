from abc import ABCMeta, abstractmethod
import copy

class GeneralSolver(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.open = []
        self.closed = []
        self.successorCount = 0
        self.nodesProcessed = 0
        self.currentSearchNode = None
        self.type = ""

    @abstractmethod
    def genInitialNode(self):
        pass

    @abstractmethod
    def arcCost(self, node1, node2):
        pass

    @abstractmethod
    def updateVisuals(self):
        pass

    def search(self, type = "best"):

        self.type = type.lower()
        if (self.type == "best" or self.type == "bredth" or self.type == "depth"):
            pass
        else:
            print("Error in search type!")
            print("Got: " + self.type)
            return None

        print("Searching for solution...")

        self.open = []
        self.closed = []

        self.open.append(self.genInitialNode())

        # Statisitics
        self.successorCount = 0
        self.nodesProcessed = 0

        tt = 1
        while (True):
            print("Open: " + str(self.open))
            tt += 1
            if not self.open:
                print("open empty")
                return None

            X = self.open.pop(0)

            self.nodesProcessed += 1
            self.currentSearchNode = copy.deepcopy(X)

            # update visual
            #self.currentSearchNode = copy.deepcopy(X)
            #self.updateVisuals()

            self.closed.append(X)
            X.open = False
            if(X.isSolution()):
                print("\n-------------\n| Finished! |\n-------------\n\nTotal nodes pocessed: " + str(self.nodesProcessed) + "\nTotal sucessors generated: " + str(self.successorCount) + "\n\nFinal path:")
                return X
            successors = X.genAllSuccessors()
            print("vksndsmd: " + str(successors))
            self.successorCount += len(successors)

            for i in range(len(successors)):
                s = successors[i]
                newS = self.existsInOpenOrClosed(s)
                if newS is not None:
                    s = newS

                X.children.append(s)
                if self.existsInOpenOrClosed(s) is None:
                    self._attacheAndEval(s, X)
                    if self.type == "best":
                        self.open.append(s)
                        self.open = sorted(self.open, key=lambda x: x.f)
                    elif self.type == "depth":
                        self.open = [s] + self.open
                    elif self.type == "bredth":
                        self.open.append(s)
                    else:
                        print("Something went wrong, search type not correctly checked")
                        return None
                elif X.g + self.arcCost(s, X) < s.g:
                    self._attacheAndEval(s, X)
                    if not s.open:
                        self.propagatePathImprovments(s)

        print("out of while")
        return None


    def _attacheAndEval(self, child, parent):
        child.parent = parent
        child.g = parent.g + self.arcCost(parent, child)
        child.setF()

    def propagatePathImprovments(self, node):
        for child in node.children:
            if node.g + self.arcCost(node, child) < child.g:
                child.parent = node
                child.g = node.g + self.arcCost(node, child)
                self.propagatePathImprovments(child)

    def existsInOpenOrClosed(self, node):
        for o in self.open:
            if o.state.id == node.state.id:
                return o

        for c in self.closed:
            if c.state.id == node.state.id:
                return c

        return None

