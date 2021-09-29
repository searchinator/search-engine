import bisect

from line_storage import LineStorage


class Alphabetize:
    def __init__(self, lineStorage: LineStorage):
        self.lineStorage = lineStorage


    def sortNewList(self, csList):
        # csList.sort(key=str.casefold)
        return sorted(csList, key=str.casefold)


    def mergeSort(self):
        # sortedList is the complete sorted list of CS lines
        # for every input given so far
        sortedList = self.lineStorage.getAlphaList()
        # csList holds the sorted list of CS lines only 
        # for the current input
        csList = self.sortNewList(self.lineStorage.getCSList()) 
        newList = []
        i = 0
        j = 0
        while i < len(csList) and j < len(sortedList):
            if csList[i] < sortedList[j]:
                newList.append(csList[i])
                i += 1
            else:
                newList.append(sortedList[j])
                j += 1
        while i < len(csList):
            newList.append(csList[i])
            i += 1
        while j < len(sortedList):
            newList.append(sortedList[j])
            j += 1
        self.lineStorage.updateAlphaList(newList)

    """
    Methods below this line are no longer used.
    """
    def addLines(self, newItems, sortedList):
        if len(newItems) >= len(sortedList)/2:
            self.__merge(newItems, sortedList)
        else:
            self.__insert(newItems, sortedList)


    def __insert(self, newItems, sortedList):
        for i in newItems:
            # for each item, do a binary insert
            bisect.insort(sortedList, i)


    def __merge(self, newItems, sortedList):
        sortedList.extend(newItems)
        sortedList.sort(key=str.casefold)
