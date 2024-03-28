from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')
def index():
    new = [
    {
    'Title': 'Title1',
    'Description': 'Description1',
    'Date': '01.01.2024'
    },
    {
    'Title': 'Title2',
    'Description': 'Description2',
    'Date': '02.01.2024'
    },
    {
    'Title': 'Title3',
    'Description': 'Description3',
    'Date': '03.01.2024'
    }
    ]
    context = {
    'news': new
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()