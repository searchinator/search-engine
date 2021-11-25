from flask import Flask, request
from flask_cors import CORS

from alphabetize import Alphabetize
from circular_shift import CircularShift
from engine import Engine
from line_storage import LineStorage
from repository import Repository

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

line_storage = LineStorage()
circular_shifter = CircularShift()
alphabetizer = Alphabetize()
repository = Repository()
engine = Engine()


@app.route('/circular-shift', methods=['POST'])
def circular_shifting():
    line_storage.reset_for_new_input()
    line = request.json['line']
    line_storage.insert_input(line)
    circular_shifter.shift(line)
    temp_list = line_storage.get_cs_list()
    return {'csLines': temp_list}


''' NOW DEFUNCT
@app.route('/alphabetize', methods=['GET'])
def sort_lines():
    abt.merge_sort()
    temp_list = line_storage.getAlphaList()
    return {'alphaLines': temp_list}
'''


@app.route('/url', methods=['POST'])
def add_url_desc():
    url = request.json['url']
    desc = request.json['desc']
    engine.insert_new(url, desc)
    return {"response": 'Inserted URL {0} with description {1}'.format(url, desc)}


@app.route('/search', methods=['GET', 'POST'])
def get_doc():
    search_query = request.args.get('query')
    page_size = request.json['page_size']
    page_num = request.json['page_num']
    print(search_query)
    result = repository.search_docs_with_key(search_query, page_size, page_num)
    print(result)
    return result


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
