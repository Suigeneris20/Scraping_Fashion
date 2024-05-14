from flask import Flask
from _testScraper import return_data

app = Flask(__name__)

@app.route('/data/')
def get_data():
    return return_data()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
