from flask import *

app = Flask(__name__)

@app.route('/shows', methods=['POST'])
def add_show():
    pass

if __name__ == '__main__':
    app.run()
