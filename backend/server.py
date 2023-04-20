from flask import Flask
from report import *

app = Flask(__name__)

@app.route('/report/<string:id>')
def report(id):
    return getReport(id)

if __name__ == "__main__":
    app.run(debug=True)