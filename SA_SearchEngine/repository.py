from bson import json_util
from pymongo import MongoClient

import query_makers


class Repository:

    def __init__(self):
        # connects to the local instance of mongodb. Make sure you have one installed
        self.client = MongoClient("mongodb://localhost:27017")
        # sets 'db' to point to the 'searchinator' database.
        self.db = self.client.searchinator
        self.query_maker = query_makers.DefaultQueryMaker()  # TODO use query_makers.LogicalQueryMaker()

    """
    the document is stored in the 'kwic' collection
    the schema is {id, url, csLine, lookupKey}
        where:
            ID is auto generated
            lookupKey is the first non-noise word of the csLine
            TODO: list of csLines sent here should not begin with noise words
    """

    def insert_doc(self, cs_lines, url_id):
        for cs_line in cs_lines:
            doc = {
                'url_id': url_id,
                'acsDescription': cs_line,
                'lookupKey': cs_line.split(" ")[0]
            }
            result = self.db.kwic.insert_one(doc)
            print('Inserted CSLine {0} for URL ID {1} with ID {2}'.format(
                cs_line, url_id, result.inserted_id))

    def insert_url(self, url):
        doc = {
            'url': url
        }
        result = self.db.url.insert_one(doc)
        print('Inserted URL {0} with ID {1}'.format(url, result.inserted_id))
        return result.inserted_id

    def search_docs_with_key(self, search_key, page_size=10, page_num=1):
        skips = page_size * (page_num - 1)

        query = self.query_maker.make_query(search_key)

        cursor = self.db.kwic.find(query).skip(skips).limit(page_size)
        return json_util.dumps(cursor)
        # return [x for x in cursor]

    def get_doc(self):
        db = self.client.business
        docs = self.db.kwic.find({})
        for doc in docs:
            print(doc)
