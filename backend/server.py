from flask import Flask
from report import *
from power import *

app = Flask(__name__)

@app.route('/report/<string:id>')
def report(id):
    return getReport(id)

@app.route('/power/<string:id>')
def power(id):
    return getSwellPower(id)

if __name__ == "__main__":
    app.run(debug=True)