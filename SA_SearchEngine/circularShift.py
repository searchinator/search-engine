from line_storage import LineStorage


class CircularShift:

    def __init__(self):
        pass

    def list_to_str(self, list):
        delimiter = ' '
        ret = ''
        for item in list:
            ret += str(item) + delimiter
        return ret.rstrip()

    def circular(self, description):
        csList = []
        split = description.split(" ")
        csList.append(self.list_to_str(split))
        for i in range(1, len(split)):
            sublist = split[i:len(split)]
            sublist.extend(split[:i])
            csList.append(self.list_to_str(sublist))
        return csList
