class LineStorage:

    def __init__(self):
        self.input = ""
        self.cs_list = []
        self.alpha_list = []

    def insert_input(self, line):
        self.input = line

    def reset_for_new_input(self):
        self.input = ""
        self.cs_list = []

    def insert_cs_line(self, line):
        self.cs_list.append(line)

    def update_alpha_list(self, new_alpha_list):
        self.alpha_list = new_alpha_list

    def get_input_line(self):
        return self.input

    def get_cs_list(self):
        return self.cs_list

    def get_alpha_list(self):
        return self.alpha_list
