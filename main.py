from utils import *

from flask import Flask, render_template


app = Flask("StonksMarket")

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
