from flask import Flask, render_template, request
from circularShift import CircularShift
from alphabetize import Alphabetize
from flask_cors import CORS
from line_storage import LineStorage

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

lineStorage = LineStorage()
objt = CircularShift(lineStorage)
abt = Alphabetize(lineStorage)


@app.route('/circular-shift', methods=['POST'])
def circular_shifting():
	lineStorage.resetForNewInput()
	line = request.json['line']
	lineStorage.insertInput(line)
	# line = request.form['line'] # request.json['key']
	# temp_list = objt.circular()
	objt.circular()
	temp_list = lineStorage.getCSList()
	return {'csLines': temp_list}


@app.route('/alphabetize', methods=['GET'])
def sortLines():
	# cs_line = abt.addLines(temp_list, cs_lines)
	abt.mergeSort()
	temp_list = lineStorage.getAlphaList()
	return {'alphaLines': temp_list}
