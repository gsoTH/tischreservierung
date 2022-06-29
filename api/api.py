import flask
from flask import jsonify
from flask import request
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True #Zeigt Fehlerinformationen im Browser, statt nur einer generischen Error-Message


@app.route('/', methods=['GET'])
def home():
    return "<h1>Tischreservierung</h1>"

# aufruf: http://127.0.0.1:5000/api/v1/anfragen?zeitpunkt=2022-02-02 18:30:00
@app.route('/api/v1/anfragen',  methods=['GET'])
def anfragen():
    query_parameters = request.args 
    # The parsed URL parameters (the part in the URL after the question mark).
    # MultiDict[str, str]
    zeitpunkt = query_parameters.get('zeitpunkt')
    if not zeitpunkt: #Falls kein Parameter angegeben wurde
        return bad_request("Kein Zeitpunkt angegeben")
#    if validateDateTimeFormat(zeitpunkt) == False:
#        return bad_request("Zeitformat entspricht nicht dem Internetformat")

#    zeitpunkt = zeitpunktAnpassen(zeitpunkt)
    
    subquery = "SELECT tischNr FROM reservierungen WHERE zeitpunkt LIKE '" + zeitpunkt +"'"
    query = "SELECT nr, anzahlPlaetze FROM tische WHERE nr NOT IN (" + subquery +");"

    conn = sqlite3.connect('api/buchungssystem.sqlite')
    conn.row_factory = dict_factory

    # https://www.tutorialspoint.com/python_data_access/python_sqlite_cursor_object.htm
    cur = conn.cursor()
    results = cur.execute(query).fetchall()

    return jsonify(results), 200

#TODO Docstring Formate für Python nachschauen
#Formt die Ausgabe von SQLite in ein brauchbares Format um
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def validateDateTimeFormat(dateTime:str):
    #regex for InternetTimeFormat: /^[0-9]{4}-[0-1][0-9]-[0-3][0-9]T[0-2][0-9]:[0-5][0-9]:[0-5][0-9].[0-9][0-9]Z$/g
    # https://regex101.com/r/xz7hfg/1
    return NotImplementedError()

def zeitpunktAnpassen(dateTime:str):
    return NotImplementedError()

@app.route('/api/v1/reservieren',  methods=['GET'])
def reservieren():
    return not_implemented(501)

@app.route('/api/v1/stornieren',  methods=['GET'])
def stornieren():
    return not_implemented(501)

@app.errorhandler(400)
def bad_request(message):
    return "<h1>400</h1><p>"+ message + "</p>", 400

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.errorhandler(501)
def not_implemented(e):
    return "<h1>501</h1><p>Not (yet) implemented.</p>", 501

app.run()