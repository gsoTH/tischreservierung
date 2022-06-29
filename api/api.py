import flask
from flask import request   # wird benötigt, um die HTTP-Parameter abzufragen
from flask import jsonify   # übersetzt python-dicts in json
import sqlite3
import random               # notwendig für das Erzeugen eines pins
import re                   # notwendig für die Arbeit mit Regex

app = flask.Flask(__name__)
app.config["DEBUG"] = True  # Zeigt Fehlerinformationen im Browser, statt nur einer generischen Error-Message


@app.route('/', methods=['GET'])
def home():
    return "<h1>Tischreservierung</h1>"


@app.route('/api/v1/anfragen', methods=['GET'])
def anfragen():
    """ Bsp. Aufruf
    http://127.0.0.1:5000/api/v1/anfragen?zeitpunkt=2022-02-02 18:15:00
    """
    query_parameters = request.args     # The parsed URL parameters (the part in the URL after the question mark).
                                        # MultiDict[str, str]

    zeitpunkt = query_parameters.get('zeitpunkt')
    if not zeitpunkt:  # true, falls kein Parameter angegeben wurde
        return "Kein Zeitpunkt angegeben", 400
    if validateDateTimeFormat(zeitpunkt) == False:
        return "Zeitformat entspricht nicht dem erwarteten Format", 400

    zeitpunkt = zeitpunktAnpassen(zeitpunkt)

    subquery = "SELECT tischnummer FROM reservierungen WHERE zeitpunkt LIKE '" + zeitpunkt + "' AND storniert = 'False'"  # alle belegten Tische zum Zeitpunkt X
    query = "SELECT tischnummer, anzahlPlaetze FROM tische WHERE tischnummer NOT IN (" + subquery + ");"

    conn = sqlite3.connect('api/buchungssystem.sqlite')
    conn.row_factory = dict_factory

    cur = conn.cursor()  # https://www.tutorialspoint.com/python_data_access/python_sqlite_cursor_object.htm
    results = cur.execute(query).fetchall()
    conn.close()

    return jsonify(results), 200


def dict_factory(cursor, row):
    """Formt die Ausgabe von SQLite in ein brauchbares Format um"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def validateDateTimeFormat(dateTime: str):
    """Überprüft, ob ein DateTime-String einem bestimmten Muster entspricht."""
    # Regex-Muster: https://regex101.com/r/xz7hfg/1
    regPatternInternetTimeFormat = "^[0-9]{4}-[0-1][0-9]-[0-3][0-9]T[0-2][0-9]:[0-5][0-9]:[0-5][0-9].[0-9][0-9]Z$"
    retPatternSqliteTimeFormat = "^[0-9]{4}-[0-1][0-9]-[0-3][0-9] [0-2][0-9]:[0-5][0-9]:[0-5][0-9]"

    isInternetTimeFormat = re.search(regPatternInternetTimeFormat, dateTime)
    isSqliteTimeFormat = re.search(retPatternSqliteTimeFormat, dateTime)

    if isInternetTimeFormat or isSqliteTimeFormat:
        return True

    return False


def zeitpunktAnpassen(dateTime: str):
    """
    Verändert einen DateTime-String so, dass der Zeitpunkt zur halben Stunde beginnt.
    2022-02-02 18:17:00 --> 2022-02-02 18:30:00
    """
    # Regex-Muster: https://regex101.com/r/7u8IpB/1
    regPatternMinutes = ":[0-5][0-9]:"
    result = re.sub(regPatternMinutes, ":30:", dateTime)
    return result


@app.route('/api/v1/reservieren', methods=['GET'])
def reservieren():
    """Bsp. für Aufruf:
    http://127.0.0.1:5000/api/v1/reservieren?zeitpunkt=2022-02-02 18:15:00&tischnummer=4
    """
    query_parameters = request.args

    zeitpunkt = query_parameters.get('zeitpunkt')
    if not zeitpunkt:  # Falls kein Parameter angegeben wurde
        return "Kein Zeitpunkt angegeben", 400
    if validateDateTimeFormat(zeitpunkt) == False:
        return "Zeitformat entspricht nicht dem Internetformat", 400
    zeitpunkt = zeitpunktAnpassen(zeitpunkt)

    tischnummer = query_parameters.get('tischnummer')
    if not tischnummer:  # Falls kein Parameter angegeben wurde
        return "Keine Tischnummer angegeben", 400

    subquery = "SELECT tischnummer FROM reservierungen WHERE zeitpunkt LIKE '" + zeitpunkt + "' AND storniert = 'False'"  # alle belegten Tische zum Zeitpunkt X
    query = "SELECT tischnummer FROM tische WHERE tischnummer NOT IN (" + subquery + ") AND tischnummer = " + tischnummer

    conn = sqlite3.connect('api/buchungssystem.sqlite')
    conn.row_factory = dict_factory

    cur = conn.cursor()
    result = cur.execute(query).fetchone()

    if not result:  # result ist null, falls die query kein Ergebnis liefert
        return "Tisch ist nicht verfügbar.", 400

    query = "INSERT INTO reservierungen (zeitpunkt, tischnummer, pin, storniert) VALUES ('" + zeitpunkt + "', " + tischnummer + ", '" + str(
        random.randint(1111, 9999)) + "', 'False')"
    cur.execute(query)
    conn.commit()  # Änderungen in Datenbank schreiben

    query = "SELECT * FROM reservierungen WHERE zeitpunkt = '" + zeitpunkt + "' AND tischnummer = " + tischnummer + " AND storniert = 'False'"
    result = cur.execute(query).fetchone()
    conn.close()
    return jsonify(result), 200


@app.route('/api/v1/stornieren', methods=['POST'])
def stornieren():
    if not request.is_json:
        return "Request was not JSON", 400

    reservierungsnummer = request.json.get("reservierungsnummer")
    pin = request.json.get("pin")

    query = "SELECT * FROM reservierungen WHERE reservierungsnummer = " + str(
        reservierungsnummer) + " AND pin = " + str(pin)

    conn = sqlite3.connect('api/buchungssystem.sqlite')
    conn.row_factory = dict_factory

    cur = conn.cursor()
    result = cur.execute(query).fetchone()
    if not result:
        return "Reservierungsnummer und/oder PIN sind nicht korrekt", 400

    query = "UPDATE reservierungen SET storniert = 'True' WHERE reservierungsnummer = " + str(reservierungsnummer)
    cur.execute(query)
    conn.commit()
    conn.close()

    return "Die Reservierung wurde storniert", 201


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run()
