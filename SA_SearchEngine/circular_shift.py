class CircularShift:

    def __init__(self):
        pass

    def list_to_str(self, in_list):
        delimiter = ' '
        ret = ''
        for item in in_list:
            ret += str(item) + delimiter
        return ret.rstrip()

    def shift(self, description):
        cs_list = []
        split = description.split(" ")
        cs_list.append(self.list_to_str(split))
        for i in range(1, len(split)):
            sublist = split[i:len(split)]
            sublist.extend(split[:i])
            cs_list.append(self.list_to_str(sublist))
        return cs_list
