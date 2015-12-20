from abc import ABCMeta, abstractmethod

class GeneralSearchNode(object):

    __metaclass__ = ABCMeta

    def __init__(self, state):
        self.state = state
        self.open = True
        self.g = 0
        self.h = self._h()
        self.f = self.setF()
        self.parent = None
        self.children = []

    def setF(self):
        self.f = self.g + self.h

    @abstractmethod
    def _h(self):
        pass

    @abstractmethod
    def isSolution(self):
        pass

    @abstractmethod
    def genAllSuccessors(self):
        pass
