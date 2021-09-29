class sortThem:
    def alphabetize(newItems, sortedList):
        sortedList.extend(newItems)
        return sorted(sortedList, key=str.casefold)