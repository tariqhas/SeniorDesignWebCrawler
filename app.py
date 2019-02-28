from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/localcrawltest/')
def localcrawltest():
    return 'placeholder'

@app.route('/index/')
def index():
    example = { 1: {'name':'Mock Button'}, 2: {'name':'Mock Button'}, 3: {'name':'Mock Button'}}
    return render_template('index.html', example = example)\

@app.route('/executor/')
def executor():
    navi = {
                        1:{
                         'name': 'Example Value 1',
                         'value': 1,
                         },
                        2:{
                        'name': 'Example Value 2',
                        'value': 2,
                         },
                        3:{
                        'name': 'Example Value 3',
                        'value': 3,
                         },
                        4:{
                        'name': 'Example Value 4',
                        'value': 4,
                         },
                        5:{
                        'name': 'Example Value 5',
                        'value': 5,
                         }
                    }
    return render_template('executor.html', navigation = navi)

@app.route('/upload/')
def upload():
    return render_template('upload.html')

@app.route('/admin/')
def admin():
    return render_template('admin.html')

@app.route('/search/')
def search():
    return render_template('search.html')
