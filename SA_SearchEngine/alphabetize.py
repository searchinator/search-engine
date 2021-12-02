class Alphabetize:

    stop_words = {'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there',
                  'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they',
                  'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into',
                  'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who',
                  'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below',
                  'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me',
                  'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our',
                  'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she',
                  'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and',
                  'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then',
                  'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not',
                  'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too',
                  'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't',
                  'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how',
                  'further', 'was', 'here', 'than'}

    def __init__(self):
        pass

    def list_to_str(self, in_list):
        delimiter = ' '
        ret = ''
        for item in in_list:
            ret += str(item) + delimiter
        return ret.rstrip()

    def sort_new_list(self, cs_lists):
        # csList.sort(key=str.casefold)
        self.remove_stop_words_and_concatenate(cs_lists)
        cs_lists = [self.list_to_str(x) for x in cs_lists]
        return sorted(cs_lists, key=str.casefold)

    """
    This method removes any stop words at the
    beginning of the sentence, i.e., it continues
    to remove words at the beginning of list as long
    as the words are a part of the stop word list.
    """

    def remove_stop_words_and_concatenate(self, cs_lists):
        for list_idx, cs_list in enumerate(cs_lists):
            for idx, word in enumerate(cs_list):
                if word.lower() not in Alphabetize.stop_words:
                    cs_list = cs_list[idx:]
                    cs_lists[list_idx] = cs_list
                    break
