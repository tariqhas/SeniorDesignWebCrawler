from flask import Flask, render_template, abort, request, jsonify

app = Flask(__name__)

ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/index')
def index():

    # At this point, we need to pull all of the ruleset names and psudo-keys
    rulesets = {1: {'name': 'Furniture'}, 2: {'name': 'Cars'}, 3: {'name': 'Phones'}, 4: {'name': 'Watches'}}

    return render_template('index.html', rulesets=rulesets)

@app.route('/search')
def emptySearch():
    return abort(404)

@app.route('/search/<ruleset>')
def showSearch(ruleset=None):

    # At this point, we need to pull the data from the DB and build a data table from it using the ruleset selected

    header = ['Name', 'Position', 'Office', 'Age', 'Start date', 'Salary'] # example header

    data = {1: {'Name': 'Joshua Kirby', 'Position': 'BS SwE Student', 'Office': 'Fredericton', 'Age': '22?', 'Start date': '2019/01/26', "Salary": '$0'}} # example data

    return render_template("results.html", header=header, data=data)

@app.route('/admin')
def admin():
    # There should be authentication here but it's not to make dev easier

    return render_template('admin.html')

@app.route('/executor')
def executor():

    # There should be data built to show all the rule and url sets

    rulesets = {1: {'name': 'Furniture'}, 2: {'name': 'Cars'}, 3: {'name': 'Phones'}, 4: {'name': 'Watches'}}

    urlsets = {1: {'name': 'Wikipedia'}, 2: {'name': 'AutoTrader'}, 3: {'name': 'Phone Websites'}, 4: {'name': 'The Fifth Watches'}, 5: {'name': 'Government of Canada'}, 6: {'name': 'Fake Websites'}, 7: {'name': 'Line Filler'}, 8: {'name': 'Images of Cats'}}

    return render_template('executor.html', rulesets=rulesets, urlsets=urlsets)

@app.route('/run')
def run():

    ruleset = request.args.get('Ruleset')
    urlset = request.args.get('URLset')

    # Trigger the crawl somehow ¯\_(ツ)_/¯

    return executor()

@app.route('/upload')
def upload():
    return render_template('/upload.html')

@app.route('/file', methods=['POST'])
def file():

    val = request
    if 'file' not in request.files:
        error = "Missing data source!"
        return jsonify({'error': error})

    file = request.files['file']

    file.save('/home/joshua/Desktop/ExampleUpload')

    f = open(file)

    return upload()


@app.route('/localcrawltest/')
def localcrawltest():
    return 'placeholder'

@app.errorhandler(404)
def errors():
    return "Oops, this should be a page but isn't!"