# Searchinator Search Engine

## Setup

1. Install the requirements for the project.

```
pip install -r requirements.txt
```

2. [Install MongoDB](https://www.mongodb.com/try/download/community)
3. Ensure the environmental variables include MongoDB.
4. Run `mongod` to start the MongoDB server.
5. In another terminal, run `mongo` to run the MongoDB CLI.
6. Copy and paste the following to the CLI:
```
db.getCollection('kwic')
  .createIndex(
    {
      lookupKey: 1
      /*
       * Keys
       *
       * Normal index
       * fieldA:  1, //ascending
       * fieldB: -1  //descending
       *
       * Wildcard index
       * '$**': 1, //wildcard index on all fields and subfields in a document
       * 'path.to.field.$**': 1 //wildcard index on a specific field and its subpaths
       *
       * Text index
       * fieldA: 'text',
       * fieldB: 'text'
       *
       * Geospatial Index
       * locationField: '2dsphere'
       *
       * Hashed Index
       * fieldA: 'hashed'
       */
    }, {
      /*
       * Options (https://docs.mongodb.com/manual/reference/method/db.collection.createIndex/#options-for-all-index-types)
       *
       * background: true, //ignored in 4.2+
       * unique: false,
       * name: 'some name',
       * partialFilterExpression: {},
       * sparse: false,
       * expireAfterSeconds: TTL,
       * collation: {}
       */
    }
  );
```
7. Run `app.py` to start the Flask server.
8. Use [Postman](https://www.postman.com/) or run `dummy_client.py` to send requests to the server.
