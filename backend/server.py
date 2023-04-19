from flask import Flask
from report import *

app = Flask(__name__)

@app.route("/report")
def report():
    return getReport()

if __name__ == "__main__":
    app.run(debug=True)