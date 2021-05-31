from abc import ABC, abstractmethod


class ActFrame(ABC):

    def __init__(self, actType, actParams = None):
        if actType == None:
            raise Exception('actType cannot be None')
        self.__actType = actType

        if actParams != None:
            self.__actParams = actParams

    def __repr__(self):
        return str(type(self))

    def __str__(self):
        return "actType:{} actParams:{}".format(self.__actType,self.__actParams)


    def setActParams(self, actParams):
        self.__actParams = actParams

    def getActParams(self):
        return self.__actParams

    def getActType(self):
        return self.__actType
