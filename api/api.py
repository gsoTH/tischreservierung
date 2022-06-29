import flask
from flask import jsonify
from flask import request
import sqlite3
import random #notwendig für das Erzeugen eines pins
import re #notwendig für die Arbeit mit Regex


app = flask.Flask(__name__)
app.config["DEBUG"] = True #Zeigt Fehlerinformationen im Browser, statt nur einer generischen Error-Message


@app.route('/', methods=['GET'])
def home():
    return "<h1>Tischreservierung</h1>"


@app.route('/api/v1/anfragen',  methods=['GET'])
def anfragen():
    # Bsp. Aufruf : http://127.0.0.1:5000/api/v1/anfragen?zeitpunkt=2022-02-02 18:15:00
    query_parameters = request.args 
    # The parsed URL parameters (the part in the URL after the question mark).
    # MultiDict[str, str]
    zeitpunkt = query_parameters.get('zeitpunkt')
    if not zeitpunkt: #Falls kein Parameter angegeben wurde
        return bad_request("Kein Zeitpunkt angegeben")
    if validateDateTimeFormat(zeitpunkt) == False:
        return bad_request("Zeitformat entspricht nicht dem erwarteten Format")

    zeitpunkt = zeitpunktAnpassen(zeitpunkt)
    
    subquery = "SELECT tischnummer FROM reservierungen WHERE zeitpunkt LIKE '" + zeitpunkt +"'"
    query = "SELECT nr, anzahlPlaetze FROM tische WHERE nr NOT IN (" + subquery +");"

    conn = sqlite3.connect('api/buchungssystem.sqlite')
    conn.row_factory = dict_factory

    # https://www.tutorialspoint.com/python_data_access/python_sqlite_cursor_object.htm
    cur = conn.cursor()
    results = cur.execute(query).fetchall()
    conn.close()

    return jsonify(results), 200


#TODO Docstring Formate für Python nachschauen
#Formt die Ausgabe von SQLite in ein brauchbares Format um
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def validateDateTimeFormat(dateTime:str):
    # Regex-Muster: https://regex101.com/r/xz7hfg/1
    regPatternInternetTimeFormat = "^[0-9]{4}-[0-1][0-9]-[0-3][0-9]T[0-2][0-9]:[0-5][0-9]:[0-5][0-9].[0-9][0-9]Z$"
    retPatternSqliteTimeFormat = "^[0-9]{4}-[0-1][0-9]-[0-3][0-9] [0-2][0-9]:[0-5][0-9]:[0-5][0-9]"
    
    isInternetTimeFormat = re.search(regPatternInternetTimeFormat, dateTime)
    isSqliteTimeFormat = re.search(retPatternSqliteTimeFormat, dateTime)
    
    if isInternetTimeFormat or isSqliteTimeFormat:
        return True
    
    return False


def zeitpunktAnpassen(dateTime:str):
    # https://regex101.com/r/7u8IpB/1
    regPatternMinutes = ":[0-5][0-9]:"
    result = re.sub(regPatternMinutes, ":30:", dateTime)
    return result


@app.route('/api/v1/reservieren',  methods=['GET'])
def reservieren():
    #Bsp. für Aufruf: http://127.0.0.1:5000/api/v1/reservieren?zeitpunkt=2022-02-02 18:15:00&tischnummer=4
    query_parameters = request.args 
    zeitpunkt = query_parameters.get('zeitpunkt')
    if not zeitpunkt: #Falls kein Parameter angegeben wurde
        return bad_request("Kein Zeitpunkt angegeben")
    if validateDateTimeFormat(zeitpunkt) == False:
        return bad_request("Zeitformat entspricht nicht dem Internetformat")
    zeitpunkt = zeitpunktAnpassen(zeitpunkt)

    tischnummer = query_parameters.get('tischnummer')
    if not tischnummer: #Falls kein Parameter angegeben wurde
        return bad_request("Keine Tischnummer angegeben")

    subquery = "SELECT tischnummer FROM reservierungen WHERE zeitpunkt LIKE '" + zeitpunkt +"'"
    query = "SELECT nr FROM tische WHERE nr NOT IN (" + subquery +") AND nr = " + tischnummer

    conn = sqlite3.connect('api/buchungssystem.sqlite')
    conn.row_factory = dict_factory

    cur = conn.cursor()
    result = cur.execute(query).fetchone()

    if not result:
        # result ist null, falls die query kein Ergebnis liefert
        return bad_request("Tisch ist nicht verfügbar.")

    query = "INSERT INTO reservierungen (zeitpunkt, tischnummer, pin, storniert) VALUES ('"+ zeitpunkt + "', " + tischnummer + ", '" + str(random.randint(1111, 9999)) + "', 'False')"
    cur.execute(query)
    conn.commit() #Änderungen in Datenbank schreiben

    query = "SELECT * FROM reservierungen WHERE zeitpunkt = '"+ zeitpunkt +"' AND tischnummer = " + tischnummer
    result = cur.execute(query).fetchone()
    conn.close()
    return jsonify(result), 200


@app.route('/api/v1/stornieren',  methods=['POST'])
def stornieren():
   if not request.is_json:
        return "Request was not JSON", 400


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