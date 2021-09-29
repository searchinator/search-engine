import bisect

class Alphabetize:
    def __init__(self):
        pass

    def addLines(self, newItems, sortedList):
        if len(newItems) >= len(sortedList)/2:
            self.__merge(newItems, sortedList)
        else:
            self.__insert(newItems, sortedList)

        return

    def __insert(self, newItems, sortedList):
        for i in newItems:
            # for each item, do a binary insert
            bisect.insort(sortedList, i)
        return

    def __merge(self, newItems, sortedList):
        sortedList.extend(newItems)
        sortedList.sort(sortedList, key=str.casefold)
        return
