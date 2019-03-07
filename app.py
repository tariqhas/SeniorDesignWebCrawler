from flask import Flask, render_template, flash, request, redirect, url_for
from CrawlerInterface import *
from DataExportInterface import *
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
cc = CrawlerController()
db = InformationManager()

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'xls', 'xlsx', 'csv', 'psv']) # for att/doc list uploads
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

@app.route('/results/')
def results():
    return render_template('results.html')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ API Methods Below Here ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# before using this, user will need to define the attributes and document set to use.
@app.route('/api/invokecrawlerpreset/', methods = ['POST'])
def invoke_crawler_preset(docid, attid):
    doc = db.getDocumentListById(docid)
    att = db.getDocumentListById(attid)
    crawldata = cc.crawlDocuments(doc, att)
    return crawldata

@app.route('/api/uploadattributes/', methods = ['POST'])
def upload_attributes_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # TODO here, we need to parse the new file, delete it, and return the id that corresponds to the db data
            return 1 # temp value


