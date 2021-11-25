from abc import ABC, abstractmethod


class QueryMaker(ABC):
    @abstractmethod
    def make_query(self, search_key):
        pass


class DefaultQueryMaker(QueryMaker):
    def make_query(self, search_key):
        return {'$or': list(map(lambda term: {'lookupKey': term}, search_key.split(' ')))}


class LogicalQueryMaker(QueryMaker):
    def make_query(self, search_key):
        # TODO
        result = []
        split = search_key.split(' ')
        for i in range(len(split)):
            word = split[i]
            word_before = split[i - 1]
            if i > 0 and word_before == 'not':
                pass
            elif i < len(split) - 1:
                word_next = split[i + 1]
                if word == 'and':
                    pass
                elif word == 'or':
                    pass
        return result
