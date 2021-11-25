from abc import ABC, abstractmethod


class QueryMaker(ABC):
    @abstractmethod
    def make_query(self, search_key):
        pass


class DefaultQueryMaker(QueryMaker):
    def make_query(self, search_key):
        return {'$or': list(map(lambda term: {'lookupKey': term}, search_key.split(' ')))}
