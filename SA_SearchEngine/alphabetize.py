class Alphabetize:
    def __init__(self):
        pass

    def sort_new_list(self, cs_list):
        # csList.sort(key=str.casefold)
        return sorted(cs_list, key=str.casefold)

    ''' NOW DEFUNCT
    def merge_sort(self):
        # sorted_list is the complete sorted list of CS lines
        # for every input given so far
        sorted_list = self.line_storage.getAlphaList()
        # cs_list holds the sorted list of CS lines only 
        # for the current input
        cs_list = self.sort_new_list(self.line_storage.getCSList()) 
        new_list = []
        i = 0
        j = 0
        while i < len(cs_list) and j < len(sorted_list):
            if cs_list[i] < sorted_list[j]:
                new_list.append(cs_list[i])
                i += 1
            else:
                new_list.append(sorted_list[j])
                j += 1
        while i < len(cs_list):
            new_list.append(cs_list[i])
            i += 1
        while j < len(sorted_list):
            new_list.append(sorted_list[j])
            j += 1
        self.line_storage.updateAlphaList(new_list)
    '''
