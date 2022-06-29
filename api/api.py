import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Tischreservierung</h1>"

@app.route('api/v1/anfragen',  methods=['GET'])
def anfragen():
    return "anfragen()"

@app.route('api/v1/reservieren',  methods=['GET'])
def reservieren():
    return "reservieren()"

@app.route('api/v1/stornieren',  methods=['GET'])
def stornieren():
    return "stornieren()"

app.run()