from flask import Flask, request, jsonify
from circularShift import CircularShift
from alphabetize import Alphabetize
from flask_cors import CORS
from line_storage import LineStorage
from repository import Repository
from engine import Engine

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

lineStorage = LineStorage()
objt = CircularShift()
abt = Alphabetize()
repo = Repository()
engine = Engine()


@app.route('/circular-shift', methods=['POST'])
def circular_shifting():
    lineStorage.resetForNewInput()
    line = request.json['line']
    lineStorage.insertInput(line)
    objt.circular()
    temp_list = lineStorage.getCSList()
    return {'csLines': temp_list}


@app.route('/alphabetize', methods=['GET'])
def sortLines():
    abt.mergeSort()
    temp_list = lineStorage.getAlphaList()
    return {'alphaLines': temp_list}


@app.route('/url', methods=['POST'])
def add_url_desc():
    url = request.json['url']
    desc = request.json['desc']
    engine.insert_new(url, desc)
    return {"response": 'Inserted URL {0} with description {1}'.format(url, desc)}


@app.route('/search', methods=['GET', 'POST'])
def getdoc():
    search_query = request.args.get('query')
    page_size = request.json['page_size']
    page_num = request.json['page_num']
    print(search_query)
    result = repo.search_docs_with_key(search_query, page_size, page_num)
    print(result)
    return result
