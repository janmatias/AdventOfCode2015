from abc import ABCMeta, abstractmethod

class GeneralState(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.id = self.genUniqueID()
        self.solved = False

    @abstractmethod
    def genUniqueID(self):
        pass
