from alphabetize import Alphabetize
from circular_shift import CircularShift
from repository import Repository


class Engine:

    def __init__(self):
        self.circular_shifter = CircularShift()
        self.alphabetizer = Alphabetize()
        self.repository = Repository()

    def insert_new(self, url, description):
        cs_lines = self.circular_shifter.shift(description)
        alpha_lines = self.alphabetizer.sort_new_list(cs_lines)
        url_id = self.repository.insert_url(url)
        self.repository.insert_doc(alpha_lines, url_id)
