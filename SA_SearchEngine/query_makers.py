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
        result = []
        relation_for_index = {}
        split = search_key.split(' ')
        for i in range(1, len(split)):
            word = split[i]
            word_before = split[i - 1]
            if i > 0 and word_before.lower() == 'not':
                relation = {'$not': [{'lookupKey': word}]}
                relation_for_index[i] = relation
                result.append(relation)
        for i in range(1, len(split) - 1):
            word_before = split[i - 1]
            word = split[i]
            word_next = split[i + 1]
            if (word.lower() == 'and' or word.loser() == 'or') and i - 1 in relation_for_index:
                prev_relation = relation_for_index[i - 1]
                relation = {'$' + word.lower(): [prev_relation, {'lookupKey': word_next}]}
                result.remove(prev_relation)
                result.append(relation)
            elif (word.lower() == 'and' or word.loser() == 'or') and i - 1 not in relation_for_index:
                relation = {'$' + word.lower(): [{'lookupKey': word_before}, {'lookupKey': word_next}]}
                relation_for_index[i - 1] = relation
                result.append(relation)
            elif word_before.lower() != 'not' and word_before.lower() != 'and' and word_before.lower() != 'or':
                result.append({'lookupKey': word})
        if len(split) > 2:
            if len(split) - 3 not in relation_for_index:
                result.append({'lookupKey': split[-1]})
        else:
            result.append({'lookupKey': split[-1]})
        return {'$or': result}
