from line_storage import LineStorage

class CircularShift:

    def __init__(self, lineStorage: LineStorage):
        self.lineStorage = lineStorage

    def list_to_str(self, list):
        delimiter = ' '
        ret = ''
        for item in list:
            ret += str(item) + delimiter
        return ret.rstrip()

    def circular(self):
        # circular_shifted_lists = []
        # circular_shifted_lists.append(self.list_to_str(split))
        split = self.lineStorage.getInputLine().split(" ")
        self.lineStorage.insertCSLine(self.list_to_str(split))
        for i in range(1, len(split)):
            sublist = split[i:len(split)]
            sublist.extend(split[:i])
            # circular_shifted_lists.append(self.list_to_str(sublist))
            self.lineStorage.insertCSLine(self.list_to_str(sublist))
        # return circular_shifted_lists
        