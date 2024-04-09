import flask
from flask import Flask

app = Flask(__name__)

@app.route('/amitesh')
def welcome():  # put application's code here
    return 'Hello Amitesh 3!'


app.run(debug=True)
