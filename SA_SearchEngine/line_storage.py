class LineStorage:

    def __init__(self):
        self.input = ""
        self.csList = []
        self.alphaList = []


    def insertInput(self, line):
        self.input = line

    def resetForNewInput(self):
        self.input = ""
        self.csList = []


    def insertCSLine(self, line):
        self.csList.append(line)


    def updateAlphaList(self, newAlphaList):
        self.alphaList = newAlphaList


    def getInputLine(self):
        return self.input


    def getCSList(self):
        return self.csList


    def getAlphaList(self):
        return self.alphaList
