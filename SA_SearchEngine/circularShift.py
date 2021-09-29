class circularShift:

    def __init__(self):
        pass

    def list_to_str(self, list):
        delimiter = ' '
        ret = ''
        for item in list:
            ret += str(item) + delimiter
        return ret.rstrip()

    def circular(self, line):
        circular_shifted_lists = []
        split = line.split(" ")
        circular_shifted_lists.append(self.list_to_str(split))
        for i in range(1, len(split)):
            sublist = split[i:len(split)]
            sublist.extend(split[:i])
            circular_shifted_lists.append(self.list_to_str(sublist))
        return circular_shifted_lists
        