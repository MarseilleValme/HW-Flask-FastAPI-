from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('basetemp.html')


@app.route('/cloth/')
def cloth():
    return render_template('cloth.html')


@app.route('/jacket/')
def jacket():
    return render_template('jacket.html')

@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


if __name__ == '__main__':
    app.run()