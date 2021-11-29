from pymongo import MongoClient
import certifi
from bson import json_util
from pymongo import MongoClient

import query_makers


class Repository:

    def __init__(self):
        # connects to the local instance of mongodb. Make sure you have one installed
        self.client = MongoClient(
            "mongodb+srv://searchinator:rainbow12345@cluster0.ftay9.mongodb.net/searchinator?retryWrites=true&w=majority", tlsCAFile=certifi.where())
        # sets 'db' to point to the 'searchinator' database.
        self.db = self.client.searchinator
        # TODO use query_makers.LogicalQueryMaker()
        self.query_maker = query_makers.DefaultQueryMaker()

    """
    the document is stored in the 'kwic' collection
    the schema is {id, url, csLine, lookupKey}
        where:
            ID is auto generated
            lookupKey is the first non-noise word of the csLine
            TODO: list of csLines sent here should not begin with noise words
    """

    def insert_doc(self, cs_lines, meta_id):
        for cs_line in cs_lines:
            doc = {
                'meta_id': meta_id,
                'acsDescription': cs_line,
                'lookupKey': cs_line.split(" ")[0]
            }
            result = self.db.kwic.insert_one(doc)
            print('Inserted CSLine {0} for URL ID {1} with ID {2}'.format(
                cs_line, meta_id, result.inserted_id))

    def insert_metadata(self, url, desc):
        doc = {
            'url': url,
            'desc': desc
        }
        result = self.db.meta.insert_one(doc)
        print('Inserted URL {0} and Desc {1} with ID {2}'.format(
            url, desc, result.inserted_id))
        return result.inserted_id

    def search_docs_with_key(self, search_key, page_size=10, page_num=1):
        skips = page_size * (page_num - 1)

        query = self.query_maker.make_query(search_key)

        total_pages = self.db.kwic.count_documents(query) / 10
        cursor = self.db.kwic.find(query).skip(skips).limit(page_size)
        response = []
        for item in cursor:
            query = {'_id': item['meta_id']}
            meta = self.db.meta.find_one(query)
            res = {
                'id': item['_id'],
                'desc': meta['desc'],
                'url': meta['url'],
            }
            response.append(res)
        client_res = {'queryResult': response,
                      'total_pages': round(total_pages)}
        return json_util.dumps(client_res)
