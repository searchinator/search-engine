from circularShift import CircularShift
from alphabetize import Alphabetize
from repository import Repository


class Engine:

    def __init__(self):
        self.csShit = CircularShift()
        self.alpha = Alphabetize()
        self.repo = Repository()

    def insert_new(self, url, description):
        csLines = self.csShit.circular(description)
        alphaLines = self.alpha.sortNewList(csLines)
        url_id = self.repo.insert_url(url)
        self.repo.insert_doc(csLines, url_id)
        # TODO: remove noise from the start of the sentences
