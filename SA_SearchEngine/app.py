from flask import Flask, render_template, request
from circularShift import circularShift
from sorting import sortThem
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})

cs_lines = []
temp_list = []
objt = circularShift()


@app.route('/')
def main_page():
	return render_template('index.html')


@app.route('/circular-shift', methods=['POST'])
def circular_shifting():
	global temp_list
	line = request.json['line']
	# line = request.form['line'] # request.json['key']
	temp_list = objt.circular(line)
	return {'csLines': temp_list}


@app.route('/alphabetize', methods=['GET'])
def sortLines():
	# print(cs_lines)
	cs_line = sortThem.alphabetize(temp_list, cs_lines)
	return {'alphaLines': cs_line}
