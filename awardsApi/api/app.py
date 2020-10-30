import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

awards = [
    {'id': 17727,
     'title': 'Associate Software Engineer',
     'award': 'Star of the Unit'},
    {'id': 17728,
     'title': 'Software Engineer',
     'award': 'Spot Award'},
    {'id': 17728,
     'title': 'Software Tester',
     'award': 'Ace Award'}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hexaware Awards Night</h1><p>This is a API site to facilitate awards.</p>"

@app.route('/awards/all', methods=['GET'])
def empAll():
    return jsonify(awards)

@app.route('/awards/empid',methods=['GET'])
def empId():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for award in awards:
        if award['id'] == id:
            results.append(award)

    return jsonify(results)

app.run()