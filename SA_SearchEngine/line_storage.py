class LineStorage:

    def __init__(self):
        self.input = ""
        self.csList = []
        self.alphaList = []


    def insertInput(self, line):
        self.input = line


    def insertCSLine(self, line):
        self.csList.append(line)


    def insertAlphaLine(self, line):
        self.alphaList.append(line)


    def getInputLine(self):
        return self.input


    def getCSList(self):
        return self.csList


    def getAlphaList(self):
        return self.alphaList

